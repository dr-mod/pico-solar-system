from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_RGB565
from pimoroni import Button, RGBLED
import time
import math
import gc
import machine
from micropython import const

gc.enable()
backlight = 0.7
plusDays = 0
change = 0

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0, pen_type=PEN_RGB565)
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)
led = RGBLED(6, 7, 8)
led.set_rgb(0,0,0)



def circle(xpos0, ypos0, rad):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        display.pixel(xpos0 + x, ypos0 + y)
        display.pixel(xpos0 + y, ypos0 + x)
        display.pixel(xpos0 - y, ypos0 + x)
        display.pixel(xpos0 - x, ypos0 + y)
        display.pixel(xpos0 - x, ypos0 - y)
        display.pixel(xpos0 - y, ypos0 - x)
        display.pixel(xpos0 + y, ypos0 - x)
        display.pixel(xpos0 + x, ypos0 - y)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)


def check_for_buttons():
    global backlight
    global plusDays
    global change
    if button_x.is_pressed:
        backlight += 0.05
        if backlight > 1:
            backlight = 1
        display.set_backlight(backlight)
    elif button_y.is_pressed:
        backlight -= 0.05
        if backlight < 0:
            backlight = 0
        display.set_backlight(backlight)
    if button_a.is_pressed and button_b.is_pressed:
        plusDays = 0
        change = 2
        time.sleep(0.2)
    elif button_a.is_pressed:
        plusDays += 86400
        change = 3
        time.sleep(0.05)
    elif button_b.is_pressed:
        plusDays -= 86400
        change = 3
        time.sleep(0.05)


def set_internal_time(utc_time):
    rtc_base_mem = const(0x4005c000)
    atomic_bitmask_set = const(0x2000)
    (year, month, day, hour, minute, second, wday, yday) = time.localtime(utc_time)
    machine.mem32[rtc_base_mem + 4] = (year << 12) | (month << 8) | day
    machine.mem32[rtc_base_mem + 8] = ((hour << 16) | (minute << 8) | second) | (((wday + 1) % 7) << 24)
    machine.mem32[rtc_base_mem + atomic_bitmask_set + 0xc] = 0x10


def main():
    global change
    import planets
    from pluto import Pluto
    set_time()

    def draw_planets(HEIGHT, ti):
        PL_CENTER = (68, int(HEIGHT / 2))
        planets_dict = planets.coordinates(ti[0], ti[1], ti[2], ti[3], ti[4])
        # t = time.ticks_ms()
        display.set_pen(display.create_pen(255, 255, 0))
        display.circle(int(PL_CENTER[0]), int(PL_CENTER[1]), 4)
        for i, el in enumerate(planets_dict):
            r = 8 * (i + 1) + 2
            display.set_pen(display.create_pen(40, 40, 40))
            circle(PL_CENTER[0], PL_CENTER[1], r)
            feta = math.atan2(el[0], el[1])
            coordinates = (r * math.sin(feta), r * math.cos(feta))
            coordinates = (coordinates[0] + PL_CENTER[0], HEIGHT - (coordinates[1] + PL_CENTER[1]))
            for ar in range(0, len(planets.planets_a[i][0]), 5):
                x = planets.planets_a[i][0][ar] - 50 + coordinates[0]
                y = planets.planets_a[i][0][ar + 1] - 50 + coordinates[1]
                if x >= 0 and y >= 0:
                    display.set_pen(display.create_pen(planets.planets_a[i][0][ar + 2], planets.planets_a[i][0][ar + 3],
                                    planets.planets_a[i][0][ar + 4]))
                    display.pixel(int(x), int(y))
        # print("draw = " + str(time.ticks_diff(t, time.ticks_ms())))

    w = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    display.set_pen(display.create_pen(0, 0, 0))
    display.clear()
    display.update()
    display.set_backlight(0.7)
    gc.collect()

    HEIGHT = const(135)

    mi = -1
    pl = Pluto(display)

    seconds_absolute = time.time()
    ti = time.localtime(seconds_absolute + plusDays)
    da = ti[2]

    draw_planets(HEIGHT, ti)
    start_int = time.ticks_ms()
    while True:
        ticks_dif = time.ticks_diff(time.ticks_ms(), start_int)
        if ticks_dif >= 1000 or time.time() != seconds_absolute:
            seconds_absolute = time.time()
            ti = time.localtime(seconds_absolute + plusDays)
            start_int = time.ticks_ms()
            ticks_dif = 0
        if change > 0:
            ti = time.localtime(seconds_absolute + plusDays)
        if da != ti[2]:
            da = ti[2]
            change = 3

        if change > 0:
            if change == 1:
                display.set_pen(display.create_pen(0, 0, 0))
                display.clear()
                draw_planets(HEIGHT, ti)
                if plusDays > 0:
                    led.set_rgb(0, 50, 0)
                elif plusDays < 0:
                    led.set_rgb(50, 0, 0)
                else:
                    led.set_rgb(0, 0, 0)
                change = 0
            else:
                change -= 1

        display.set_pen(display.create_pen(0, 0, 0))
        display.rectangle(140, 0, 100, HEIGHT)
        display.rectangle(130, 0, 110, 35)
        display.rectangle(130, 93, 110, HEIGHT - 93)

        if mi != ti[4]:
            mi = ti[4]
            pl.reset()
        pl.step(ti[5], ticks_dif)
        pl.draw()

        display.set_pen(display.create_pen(244, 170, 30))
        display.text("%02d %s %d " % (ti[2], m[ti[1] - 1], ti[0]), 132, 7, 70, 2)
        display.set_pen(display.create_pen(65, 129, 50))
        display.text(w[ti[6]], 135, 93, 99, 2)
        display.set_pen(display.create_pen(130, 255, 100))
        display.text("%02d:%02d" % (ti[3], ti[4]), 132, 105, 99, 4)
        display.update()
        check_for_buttons()
        time.sleep(0.01)


def set_time():
    try:
        import wifi_config
        set_time_ntp(wifi_config)
    except ImportError:
        ds3231
        ds = ds3231.ds3231()
        set_internal_time(ds.read_time())


def set_time_ntp(wifi_config):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("Connecting to:", wifi_config.ssid)
    wlan.connect(wifi_config.ssid, wifi_config.key)
    while not wlan.isconnected() and wlan.status() >= 0:
        print("Waiting for connection...")
        time.sleep(5)
    print(wlan.ifconfig())
    print("Pico clock:", time.localtime())
    print("Setting time via ntp...")
    import ntptime
    ntpsuccess = False
    while not ntpsuccess:
        try:
            ntptime.settime()
            print("Time set: ", time.localtime())
            ntpsuccess = True
        except:
            print("NTP failure. Retrying.")
            time.sleep(5)


time.sleep(0.5)
main()