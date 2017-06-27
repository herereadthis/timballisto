# Scheduling Tasks and Cron Jobs

### Have things done when booting up

It's done in a file called `rc.local`

```bash
sudo nano /etc/rc.local

# before the exit 0, try pasting this into the file.
# You'll see it when starting your Raspberry Pi.
echo -e '\n********\n'
echo -e '\nHello World! This is an echo from /etc/rc.local.\n'
echo -e '\n********\n'
```

### Cron Jobs: tasks running periodically

```bash
crontab -e
```

#### Examples

<table>
    <thead>
        <th>Description</th>
        <th>m</th>
        <th>h</th>
        <th>dom</th>
        <th>mon</th>
        <th>dow</th>
        <th>command</th>
        <th>full example</th>
    </thead>
    <tbody>
        <tr>
            <td>Reboot every day at 12:10AM</td>
            <td>10</td>
            <td>0</td>
            <td>*</td>
            <td>*</td>
            <td>*</td>
            <td>sudo reboot</td>
            <td>10 0 * * * sudo reboot</td>
        </tr>
        <tr>
            <td>Run a backup script every Monday at 3:00AM</td>
            <td>0</td>
            <td>3</td>
            <td>*</td>
            <td>*</td>
            <td>Mon</td>
            <td>/backup_script.sh</td>
            <td>0 3 * * Mon /backup_script.sh</td>
        </tr>
        <tr>
            <td>Run a Python script at 10AM & 10PM on weekends</td>
            <td>0</td>
            <td>10,22</td>
            <td>*</td>
            <td>*</td>
            <td>Sat,Sun</td>
            <td>python3 /my_script.py</td>
            <td>0 10,22, * *  6,0 python3 /my_script.py</td>
        </tr>
    </tbody>
</table>