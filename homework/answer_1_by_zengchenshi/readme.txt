运行命令：
 ./find_interface.pl 1ak4.pdb > find_result
python3 count_aa.py find_result > count_result

第一个命令得到计算结果文件find_result。
第二个命令通过python脚本统计A、D两条链上的氨基酸个数，输出结果count_result。