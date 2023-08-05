'''
This module defines a modified version of the tao_interface class with
a few extra features to facilitate communication with the GUI
'''
import tkinter as tk
import time

import pytao
from pytao.tao_interface import new_stdout, filter_output

class tao_interface(pytao.tao_interface):
    '''
    Provides an interface between the GUI and
    the Tao command line
    '''
    def __init__(self, mode="ctypes", init_args = "", tao_exe =  "", expect_str = "Tao>", so_lib=""):
        # DEBUG
        self.debug = False # set true to print debug messages
        # Put patterns of interest here
        self.debug_patterns = ['python plot_manage']
        if self.debug:
            print(init_args)
        ###
        pytao.tao_interface.__init__(
                self, mode=mode, init_args=init_args, tao_exe=tao_exe, expect_str=expect_str, so_lib=so_lib)
        self.message = ""
        self.message_type = "" #conveys color info to console
        self.printed = tk.BooleanVar()
        self.printed.set(False)
        # DEV PURPOSES ONLY
        self._root = self.printed._root

    def cmd_in(self, cmd_str, no_warn=False):
        '''
        Runs cmd_str at the Tao command line and returns the as a string
        Warning messages generated by this command are suppressed when
        no_warn is set True
        '''
        # DEBUG
        if self.debug:
            match = False
            if self.debug_patterns == 'All':
                match = True
            elif isinstance(self.debug_patterns, list):
                for p in self.debug_patterns:
                    if cmd_str.find(p) == 0:
                        match = True
            if match:
                current_time = time.localtime()
                y = str(current_time.tm_year)
                mo = str(current_time.tm_mon)
                if len(mo) == 1:
                    mo = '0' + mo
                day = str(current_time.tm_mday)
                if len(day) == 1:
                    day = '0' + day
                hr = str(current_time.tm_hour)
                if len(hr) == 1:
                    hr = '0' + hr
                mn = str(current_time.tm_min)
                if len(mn) == 1:
                    mn = '0' + mn
                sec = str(current_time.tm_sec)
                if len(sec) == 1:
                    sec = '0' + sec
                print(y+'-'+mo+'-'+day+' '+hr+':'+mn+':'+sec, cmd_str)
        if cmd_str.find("dev ") ==0:
            cmd_str = cmd_str[4:]
            with new_stdout() as output:
                exec(cmd_str)
            output = output.getvalue()
            output = filter_output(output)
            return output
        ###

        self.message = ""
        self.message_type = "normal" #conveys color info to console
        if cmd_str.find("single_mode") == 0:
            output = "single_mode not supported on the GUI command line"
            self.message_type = "error"
        else:
            output = pytao.tao_interface.cmd_in(self, cmd_str)

        # Parse output for error messages
        if cmd_str.find("spawn ") == 0:
            self.message += "WARNING: the spawn command is very dangerous "
            self.message += "and may cause the GUI to hang if the spawned "
            self.message += "process does not exit quickly."
            self.message_type = "error"
            self.printed.set(True)
            self.message = ""
            self.message_type = "normal"
        if output.find("[ERROR") != -1:
            self.message += "Warning: Error occurred in Tao\n"
            self.message += "The offending command: " + cmd_str + "\n"
            self.message += "The error (first 20 lines):\n"
            if len(output.splitlines()) > 20:
                for i in range(20):
                    self.message += (output.splitlines()[i]) + "\n"
            else:
                self.message += output
            self.message_type = "error"
            if not no_warn:
                self.printed.set(True)
        if (output.find("Backtrace") != -1) | \
                (output.find("SIGSEGV") != -1):
            self.message = "Error occurred in Tao, causing it to crash\n"
            self.message += "The offending command: " + cmd_str + '\n'
            self.message += "The error:\n"
            self.message += output + '\n'
            self.message_type = "fatal"
            if not no_warn:
                self.printed.set(True)
        return output

    def cmd(self, cmd_str):
        '''
        Runs cmd_str at the Tao command line and prints the output
        '''
        output = self.cmd_in(cmd_str, no_warn=True)
        self.message_type = "normal"
        self.message = output
        self.printed.set(True)
