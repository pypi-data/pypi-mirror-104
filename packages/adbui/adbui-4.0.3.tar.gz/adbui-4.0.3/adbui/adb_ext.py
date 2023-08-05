# coding=utf-8
import os
import re
import time
import logging
import tarfile
import tempfile


class AdbExt(object):
    def __init__(self, util):
        self.util = util
        self.is_minicap_ready = False
        self.width, self.height = self.get_device_size()
        self.temp_name = 'temp_{}'.format(self.util.sn)  # 临时文件名加上sn，防止多个手机多线程是有冲突
        self.temp_name = self.temp_name.replace('.', '').replace(':', '')  # 远程机器sn特殊，处理一下。如：10.15.34.56:11361
        self.temp_pc_dir_path = tempfile.gettempdir()
        self.temp_device_dir_path = '/data/local/tmp'

    def get_device_size(self):
        out = self.util.shell('wm size')  # out like 'Physical size: 1080x1920'
        out = re.findall(r'\d+', out)
        return int(out[0]), int(out[1])  # width, height

    def dump(self):
        for i in range(5):
            out = self.util.adb('exec-out uiautomator dump --compressed /dev/tty', encoding='')  # 优先使用压缩模式
            start = out.find(b'<?xml')
            if start < 0:
                out = self.util.adb('exec-out uiautomator dump /dev/tty', encoding='')  # 失败后使用正常模式
                start = out.find(b'<?xml')

            end = out.find(b'</hierarchy>') + len(b'</hierarchy>')
            if start >= 0 and end > 0:  # 检查是否有xml文档
                out = out[start: end]  # 去掉xml前后的内容
                return out
        raise NameError('dump xml fail!')

    def get_pc_temp_name(self):
        return os.path.join(self.temp_pc_dir_path, self.temp_name)

    def delete_from_device(self, path):
        self.util.shell('rm -rf {}'.format(path))

    def delete_from_pc(self, path):
        if os.path.exists(path):
            os.remove(path)

    def __minicap(self):
        if not self.is_minicap_ready:  # 检测手机中是否已有 minicap
            arg = 'ls /data/local/tmp'
            out = self.util.shell(arg)
            self.is_minicap_ready = 'minicap' in out and 'minicap.so' in out

        if not self.is_minicap_ready:  # 把 minicap 导入到手机
            logging.debug('当前 minicap 还没有 ready')
            if 'package' not in os.listdir(self.temp_pc_dir_path):  # 文件没有解压
                logging.debug('当前 minicap 还没有解压')
                dir_path = os.path.dirname(os.path.abspath(__file__))
                minicap_dir_path = os.path.join(dir_path, 'minicap')
                minicap_tgz_path = os.path.join(minicap_dir_path, 'minicap.tgz')
                tar = tarfile.open(minicap_tgz_path, "r:gz")
                tar.extractall(self.temp_pc_dir_path)
                tar.close()

            built_path = os.path.join(self.temp_pc_dir_path, 'package', 'prebuilt')
            abi = self.util.shell('getprop ro.product.cpu.abi').strip()
            sdk = self.util.shell('getprop ro.build.version.sdk').strip()
            minicap_path = os.path.join(built_path, abi, 'bin', 'minicap')
            minicap_so_path = os.path.join(built_path, abi, 'lib','android-{}'.format(sdk), 'minicap.so')
            self.push(minicap_path, '/data/local/tmp')
            self.push(minicap_so_path, '/data/local/tmp')
            self.util.shell('chmod 777 /data/local/tmp/minicap*')  # 赋予权限

        size = '{}x{}@{}x{}'.format(self.width, self.height, self.width, self.height)
        arg = 'LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P {}/0 -s'.format(size)

        out = self.util.shell('"{}"'.format(arg), encoding=None)
        out = out.replace(b'\r\n', b'\n')  # 替换 win 下的换行符，否则图片无法正常显示
        return out

    def screenshot(self, pc_path=None):
        # 先尝试 minicap 截图
        out = self.__minicap()
        if b'' == out:  # minicap 截图失败，使用 screencap 截图
            logging.warning('minicap 截图失败')
            arg = 'adb -s {} exec-out screencap -p'.format(self.util.sn)
            out = self.util.cmd(arg, encoding=None)  # 这里是 png bytes string

        # 保存截图
        if pc_path:
            if self.util.is_py2:
                pc_path = pc_path.decode('utf-8')
            self.delete_from_pc(pc_path)  # 删除电脑文件
            with open(pc_path, 'wb') as f:
                f.write(out)

        return out

    def pull(self, device_path=None, pc_path=None):
        return self.util.adb('pull "{}" "{}"'.format(device_path, pc_path))

    def push(self, pc_path=None, device_path=None):
        return self.util.adb('push "{}" "{}"'.format(pc_path, device_path))

    def click(self, x, y):
        self.util.shell('input tap {} {}'.format(x, y))

    def long_click(self, x, y, duration=''):
        """
        长按
        :param x: x 坐标
        :param y: y 坐标
        :param duration: 长按的时间（ms）
        :return:
        """
        self.util.shell('input touchscreen swipe {} {} {} {} {}'.format(x, y, x, y, duration))

    def start(self, pkg):
        """
        使用monkey，只需给出包名即可启动一个应用
        :param pkg:
        :return:
        """
        self.util.shell('monkey -p {} 1'.format(pkg))

    def stop(self, pkg):
        self.util.shell('am force-stop {}'.format(pkg))

    def input(self, text):
        self.util.shell('input text "{}"'.format(text.replace('&', '\&')))

    def back(self, times=1):
        while times:
            self.util.shell('input keyevent 4')
            times -= 1

    def home(self):
        self.util.shell('input keyevent 3')

    def enter(self, times=1):
        while times:
            self.util.shell('input keyevent 66')
            times -= 1

    def swipe(self, e1=None, e2=None, start_x=None, start_y=None, end_x=None, end_y=None, duration=" "):
        """
        滑动事件，Android 4.4以上可选duration(ms)
        usage: swipe(e1, e2)
               swipe(e1, end_x=200, end_y=500)
               swipe(start_x=0.5, start_y=0.5, e2)
        """
        if e1 is not None:
            start_x = e1[0]
            start_y = e1[1]
        if e2 is not None:
            end_x = e2[0]
            end_y = e2[1]
        if 0 < start_x < 1:
            start_x = start_x * self.width
        if 0 < start_y < 1:
            start_y = start_y * self.height
        if 0 < end_x < 1:
            end_x = end_x * self.width
        if 0 < end_y < 1:
            end_y = end_y * self.height

        self.util.shell('input swipe %s %s %s %s %s' % (str(start_x), str(start_y), str(end_x), str(end_y), str(duration)))

    def clear(self, pkg):
        """
        重置应用
        :param pkg:
        :return:
        """
        self.util.shell('pm clear {}'.format(pkg))

    def wake_up(self):
        """
        点亮屏幕
        :return:
        """
        self.util.shell('input keyevent KEYCODE_WAKEUP')

    def unlock(self):
        """
        解锁屏幕
        :return:
        """
        self.util.shell('input keyevent 82')

    def grant(self, pkg, permission):
        """
        给app赋权限，类似 adb shell pm grant [PACKAGE_NAME] android.permission.PACKAGE_USAGE_STATS
        :return:
        """
        self.util.shell('pm grant {} {}'.format(pkg, permission))

    def install(self, apk_path, with_g=True, with_r=False, user=None):
        """
        安装包
        :param apk_path:
        :param with_g: -g 在一些设备上可以自动授权，默认 true
        :param with_r: -r 覆盖安装，默认 false
        :param user:
        :return:
        """
        arg = 'install'
        if user:
            arg = arg + ' -user {}'.format(user)
        if with_g:
            arg = arg + ' -g'
        if with_r:
            arg = arg + ' -r'
        self.util.adb('{} "{}"'.format(arg, apk_path))

    def uninstall(self, pkg):
        """
        卸载包
        :param pkg:
        :return:
        """
        self.util.adb('uninstall {}'.format(pkg))

    def get_name(self, remove_blank=False):
        name = self.util.shell('getprop ro.config.marketing_name').strip()
        if not name:
            name = self.util.shell('getprop ro.product.nickname').strip()
        if remove_blank:
            name = name.replace(' ', '')
        return name

    def switch_user(self, user_id, wait_time=5):
        self.util.shell('am switch-user {}'.format(user_id))
        time.sleep(wait_time)
