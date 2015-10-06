#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring."""

#Author - Erica Liz

import argparse
import time
import urllib2


def main():
    """Main function of program."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type = str, help = 'Data file to process.')
    parser.add_argument('--servers', type = int, help = 'Number of Servers.')
    args = parser.parse_args()

    if args.file:
        try:
            get_file = simulateOneServer(args.file)
        except:
            print 'Invalid'      
    else:
        print 'Please enter another filename or URL.'


class Queue:
    """Implementing a queue to see how our data is viewed.""" #copied from text
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item): #adds new item
        self.items.insert(0, item)

    def dequeue(self): #removed fromt item
        return self.items.pop()

    def size(self): #gives how many in queue
        return len(self.items)

class Server:
    """Tracks to see current task.""" #copied from text class Printer
    def __init__(self):        
        self.current_task = None
        self.time_remaining = 0

    def tick(self): # sets to idle if task complete
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self): #when a task is in queue
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self,new_task): #time for next task
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Request:
    """Represents single printing task.""" #copied form text class Task
    def __init__(self, time, length):
        self.timestamp = time
        self.length = int(length) #int for time spent in queue

    def get_stamp(self):
        return self.timestamp #gives time stamp

    def get_length(self):
        return self.length

    def wait_time(self, cur_time): #time in queue before printing
        return cur_time - self.timestamp


def simulateOneServer(url):
    """Prints average wait time for request."""
    
    response = urllib2.urlopen(url) #opens csv file
    html = response.read() #reads the csv file
    #print html
    my_list = []

    for row in html:
        secs = int(row[0])
        #time = int(row[2]) 
        print secs



if __name__ == '__main__':
    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'
    main()
