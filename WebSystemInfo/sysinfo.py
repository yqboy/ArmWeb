# -*- coding: utf-8 -*-
import os
import psutil as p

eth = 'eth0'

def getIOinfo():
    disk_info = p.disk_io_counters(perdisk=True)

    disk_Read = {}
    disk_Write = {}
    try:
        for sd in disk_info:
            disk_Read[sd] = disk_info[sd][2] / 1024.0
            disk_Write[sd] = disk_info[sd][3] / 1024.0

        net_Send = p.net_io_counters(pernic=True)[eth].bytes_sent / 1024.0
        net_Recv = p.net_io_counters(pernic=True)[eth].bytes_recv / 1024.0
    except Exception as e:
        net_Send = net_Recv = 0.0

    return net_Send, net_Recv, disk_Read, disk_Write


def getInfo():
    # stime = time.time()
    io_data = {}
    disk_read = 0
    disk_wite = 0
    fns, fnr, fdr, fdw = getIOinfo()

    cpu_all = p.cpu_percent(1, True)
    io_data['cpu_all'] = cpu_all
    temp_cpu = 0
    for i in cpu_all:
        temp_cpu += i
    cpu_percent = temp_cpu / len(cpu_all)
    io_data['cpu_percent'] = '%.1f%%' % cpu_percent

    sns, snr, sdr, sdw = getIOinfo()

    for k in fdr:
        read = sdr[k] - fdr[k]
        wite = sdw[k] - fdw[k]
        if read >= disk_read:
            disk_read = read
        if wite >= disk_wite:
            disk_wite = wite
    net_Send = (sns - fns)
    net_Recv = (snr - fnr)

    try:
        io_data['net_ip'] = os.popen('hostname -I').read().split()[0]
    except Exception as e:
        io_data['net_ip'] = '127.0.0.1'

    if net_Send >= 1024:
        io_data['net_up'] = '%.2f Mb/s' % (net_Send / 1024.0)
    else:
        io_data['net_up'] = '%.2f Kb/s' % net_Send
    if net_Recv >= 1024:
        io_data['net_down'] = '%.2f Mb/s' % (net_Recv / 1024.0)
    else:
        io_data['net_down'] = '%.2f Kb/s' % net_Recv

    if disk_read >= 1024:
        io_data['disk_read'] = '%.2f Mb/s' % (disk_read / 1024.0)
    else:
        io_data['disk_read'] = '%.2f Kb/s' % disk_read
    if disk_wite >= 1024:
        io_data['disk_write'] = '%.2f Mb/s' % (disk_wite / 1024.0)
    else:
        io_data['disk_write'] = '%.2f Kb/s' % disk_wite

    io_data['disk_percent'] = '%s%%' % p.disk_usage('/').percent

    memory = p.virtual_memory()
    memory_total = memory.total / 1024 / 1024
    if memory_total > 1024:
        io_data['memory_total'] = '%sGB' % (memory_total / 1024)
    else:
        io_data['memory_total'] = '%sMB' % memory_total

    io_data['memory_percent'] = '%s%%' % memory.percent

    swap = p.swap_memory()
    swap_total = swap.total / 1024 / 1024
    if swap_total > 1024:
        io_data['swap_total'] = '%sGB' % (swap_total / 1024)
    else:
        io_data['swap_total'] = '%sMB' % swap_total

    io_data['swap_percent'] = '%s%%' % swap.percent

    temp_file = '/sys/class/thermal/thermal_zone0/temp'
    if os.path.exists(temp_file):
        f = open(temp_file)
        temp = int(f.read().strip('\n'))
        f.close()
        if temp > 200:
            temp = temp / 1000
        io_data['cpu_temp'] = '%s℃' % temp
    else:
        io_data['cpu_temp'] = '0℃'

    return io_data
