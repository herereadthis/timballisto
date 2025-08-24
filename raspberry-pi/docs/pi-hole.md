# Pi-hole

Pihole is an adblocking software which runs on any Linux distribution but is often runnng on a Raspberry Pi. It stops ads by using [DNS sinkholing](https://en.wikipedia.org/wiki/DNS_sinkhole) and blocklists.
* [It acts as local DNS](https://blog.cryptoaustralia.org.au/2018/08/06/why-you-need-network-wide-ad-blocker-pi-hole/) (domain name system) resolver on your network.
* Any request on your network which appear on the Pi-hole&rsquo;s blocklist do not go to their public address but just go to the Pi-hole itself (i.e., sinkhole).
* Instead, the Pi-hole will return blanks (e.g. an empty JS file for JavaScript asset request).
* To begin, `ssh` into your Raspberry Pi.
  ```
  ssh pi@RPI_HOSTNAME.local
  ```
* Run this
  ```bash
  curl -sSL https://install.pi-hole.net | bash
  ```
* Follow all the prompts. Remember to save the IP address and password
  * Recommended: when given the options of DNS, go with &ldquo;OpenDNS.&rdquo;
  * Recommended: when given the choice of blocklists, go with all of them.
* You can go to the Pihole admin either at http://pi.hole/admin or http://PIHOLE_ADDRESS/admin
* Update the password
  ```bash
  pihole -a -p
  ```

## Modify your router

### Verizon Actiontec

* Go to 192.168.1.1, which is your router.
* Enter admin and password, which is typically `admin` and a physical password sticker on the router itself.
* In the top navigation, click on the &ldquo;My Network&rdquo; icon.
* In the left menu, click on &ldquo;Network Connections&rdquo; text link.
* On the &ldquo;Network Connections&rdquo; page, click on &ldquo;Broadband Connection (Ethernet/Coax)&rdquo; text link.
* On the &ldquo;Broadband Connection (Ethernet/Coax) Properties&rdquo; page, click on the &ldquo;Settings&rdquo; button.
* In the left menu, click "Connection Properties"
* On the &ldquo;Broadband Connection (ethernet/coax) Properties&rdquo; view, click &ldquo;Settings&rdquo; button.
* For the &ldquo;DNS Server&rdquo; setting, change the option to &ldquo;Use the Following DNS Server Address.&rdquo;
* For the &ldquo;Primary DNS Server&rdquo; option, enter the IP address of the Pi-hole.
* Click the &ldquo;Apply&rdquo; button a few times until you return to the &ldquo;Network Connections&rdquo; page.

## Commands

* Version
  ```bash
  pihole version
  ```
* Update
  ```bash
  pihole -up
  ```
* Whitelist
  ```bash
  pihole -w foo.allow-domain.com
  ```
* Blacklist
  ```bash
  pihole -b bar.block-domain.com
  ```
* Admin
  ```bash
  pihole admin
  ```
* &ldquo;Chronometer&rdquo; Dashboard
  ```bash
  pihole -c
  ```


## Extra bits

* You might as well disable Wifi on the PiHole. Use Cron job.
  ```bash
  crontab -e
  # paste this at the bottom
  @reboot sudo ifdown wlan0
  ```

## Sources

* [DNS sinkhole](https://en.wikipedia.org/wiki/DNS_sinkhole) - Wikipedia
* [Why You Need a Network-Wide Ad-Blocker (Part 1)](https://blog.cryptoaustralia.org.au/2018/08/06/why-you-need-network-wide-ad-blocker-pi-hole/)
* [(Verizon FIOS) Actiontec MI424WR and Westell UltraLine](https://support.opendns.com/hc/en-us/articles/228008027--Verizon-FIOS-Actiontec-MI424WR-and-Westell-UltraLine) - OpenDNS
* [Configuring Verizon FiOs router... ](https://www.reddit.com/r/pihole/comments/5tw4mu/) - Reddit
