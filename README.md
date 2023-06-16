<h1>Introduction</h1>
monitor whether have a suspecious file in the specify directory with crontab and send alert message by telegram bot.
<br/>
my use case is monitoring the wordpress which is deployed on docker, as my wordpress site have some exploits that make others can insert some dirty files.

<h1>Usage</h1>

- `crontab -e` : execute the script per hour

  ```
  */60 * * * * python3 /path/to/monitorImWordpress.py
  ```
