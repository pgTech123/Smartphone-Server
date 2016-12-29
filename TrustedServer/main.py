import time
import proxy
import config
import urllib2
import subprocess
from multiprocessing import Process


def panic():
    print "!!!PANIC MODE!!! SAFE MODE FAILED..."
    # TODO: Safety procedure


def restart_proxy_safe(proxy_process, IN_SAFE_MODE):
    if IN_SAFE_MODE:
        panic()
        # FIXME: Maybe return so there is not a restart every time

    proxy_process.terminate()
    proxy_process = Process(target=proxy.start, args=(["-s"],))    # "-s" = Safemode
    proxy_process.start()
    IN_SAFE_MODE = True
    print "Proxy restarted in safemode"
    return [proxy_process, IN_SAFE_MODE]


def main():
    # Start proxy and call the reference page as a heartbeat.
    # If the reference page is not loaded on time, we disconnect the proxy and
    # relaunch it as a loopback.
    proxy_process = Process(target=proxy.start, args=(["-d"],))    # "-d" = Default
    proxy_process.start()

    IN_SAFE_MODE = False
    print "Proxy started"
    while 1:
        time.sleep(config.HEARTHBEAT)
        try:
            urllib2.urlopen(config.SAFEPAGE, timeout=config.ALLOWED_RESPONSE_TIME)
        except urllib2.URLError, e:
            [proxy_process, IN_SAFE_MODE] = restart_proxy_safe(proxy_process, IN_SAFE_MODE)


if __name__ == '__main__':
    main()

