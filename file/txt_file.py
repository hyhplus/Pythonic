#!/usr/bin/env python3
# -*- coding: utf-8 -*-
f = open('rrr.txt', encoding='utf8')
for i in range(143):
    a = f.readline()
    rgb_lst = a.split()
    need_str = """    <tr>
            <td bgcolor="{1}"><font size="3" color="#0"></font></td>
            <td bgcolor="#fff"><font size="3" color="#0">{0}</font></td>
            <td bgcolor="#fff"><font size="3" color="#0">{2} {3} {4}</font></td>
            <td bgcolor="#fff"><font size="3" color="#0">{1}</font></td>
    </tr>""".format(rgb_lst[0], rgb_lst[1], rgb_lst[2], rgb_lst[3], rgb_lst[4])
    print(need_str)


