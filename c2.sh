#!/bin/bash
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(docker ps -a -q)
