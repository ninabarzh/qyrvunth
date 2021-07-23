#!/usr/bin/python3

"""
Code snippets to read and understand the robots.txt file and ask 
the parser if we can scrape a given part of the target website.  
"""

# -----------------------------------------------------------------------
# Malicious bots will ignore the settings in a robots.txt file.
# We do not. Fetch robot.txt and check a target url is allowed or not.
# -----------------------------------------------------------------------

from urllib import robotparser

robot_parser = robotparser.RobotFileParser()

def prepare(robots_txt_url):
    robot_parser.set_url(robots_txt_url)

    return robot_parser.read()

def is_allowed(target_url, user_agent='*'):
    
    return robot_parser.can_fetch(user_agent, target_url)

# -----------------------------------------------------------------------
# Main to demo use
# -----------------------------------------------------------------------

robots_txt_url = 'http://example.com/robots.txt'

if __name__ == '__main__':
    prepare(robots_txt_url)
    print(is_allowed('http://example.com/'))
    print(is_allowed('http://example.com/python'))