# Amcres-DNS-Disable
A python script for stopping amcrest cameras from sending DNS requests to online servers using the requests library.

The easiest way to do this is to set all of the login info on all cams the same, fill out the password and IPs. Plug your DVR and IPC cam IPs in the respective lists.

These settings are not persistent after reboot. I have this running on a cron job every 1 hr.
