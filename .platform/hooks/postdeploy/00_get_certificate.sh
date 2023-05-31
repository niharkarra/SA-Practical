#!/usr/bin/env bash
sudo certbot -n -d karnihar.awsps.myinstance.com -d www.abc.karnihar.awsps.myinstance.com --nginx --agree-tos --email test@test.com
