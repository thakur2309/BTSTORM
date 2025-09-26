# BTStorm - Bluetooth DoS Jammer Tool 🎉📡

[![GitHub stars](https://img.shields.io/github/stars/Thakur2309/BTStorm?style=social)](https://github.com/Thakur2309/BTStorm)  
[![YouTube](https://img.shields.io/badge/YouTube-Firewall%20Breaker-red)](https://www.youtube.com/@FirewallBreaker09)  
[![Instagram](https://img.shields.io/badge/Instagram-sudo_xploit-purple)](https://www.instagram.com/sudo_xploit?igsh=MWN0YWc3N2JyenhoNw==)

**BTStorm** is an epic Bluetooth Denial-of-Service (DoS) jamming tool designed for **educational and ethical hacking purposes only**! 🎓🔒 It scans for nearby Bluetooth devices and unleashes an L2ping flood attack to disrupt connectivity, potentially forcing disconnections (e.g., speakers from phones). Perfect for learning Bluetooth vulnerabilities! 😎

> **⚠️ Legal Disclaimer**: This tool is for educational use in controlled environments (e.g., your own devices). Using it without permission is illegal and unethical. The author isn’t responsible for misuse. Follow local laws (e.g., FCC rules)! 🚨

### Example Output 🎥
![Instagram Image ](https://raw.githubusercontent.com/thakur2309/BTSTORM/refs/heads/main/IMG-20250926-WA0013.jpg)

<h3 align="center"> Preview!</h3>

## Features 🌟
- **Device Scanning**: Uses `hcitool` to find nearby Bluetooth devices with MACs and names. 🔍
- **Multi-Threaded Attacks**: Floods multiple devices at once with parallel threads. 💥
- **Single Device Mode**: Target any device with its MAC address. 🎯
- **Auto-Disconnect**: Tries to kick paired devices (e.g., phones) off before jamming! 🚪
- **Colorful Output**: ANSI colors make logs pop in your terminal! 🌈
- **Error Handling**: Timeouts prevent hangs during scans/attacks. ⏰
- **HCI0 Magic**: Auto-checks and enables your Bluetooth adapter (`hci0`) if down. 🛠️

## Platforms Supported 🖥️📱
BTStorm rocks on **Linux-based systems** with Bluetooth support! Here’s where it works:

### Supported Platforms
- **Kali Linux** (Recommended: BlueZ pre-installed) 🐧
- **Ubuntu/Debian** (20.04+) 🌱
- **Parrot OS** or other pentesting distros 🕵️‍♂️
- **Arch Linux** (with BlueZ package) 🏹

**Hardware Needed**: A Bluetooth adapter (built-in or USB dongle, e.g., CSR 4.0+ works great). 🔌

### Termux (Android) Support 🤖
Yes, BTStorm **works on Termux** with some tweaks! Requires **root access** (e.g., Magisk) due to Android’s Bluetooth limits.

#### Termux Requirements & Setup 📲
1. **Install Termux**: Grab it from F-Droid (not Play Store for full power). 📥
2. **Update Packages**:
3. **Install Python & Tools**:
4. **Install BlueZ**: Termux lacks BlueZ by default, so root it:
- Root your device (e.g., Magisk).
- Use `tsu` for root: `pkg install tsu`.
- Install BlueZ via chroot (advanced): `apt install bluez` (Ubuntu chroot).
- Or try: `pkg install bluez` (if available, experimental). ⚙️
5. **Bluetooth Permissions**: Enable Bluetooth in settings. For root: `su -c hciconfig hci0 up`. 🔐
6. **Run Script**: `git clone https://github.com/thakur2309/BTSTORM.git`
`cd BTSTORM`

- Use root: `tsu -c python bluetooth-jammer.py`.

**Note**: Non-rooted Termux may fail with "Permission denied". Success: 70-80% on rooted devices. Test on your speaker/headphones! 🎧

**Unsupported**: Windows/macOS (Linux-only due to `hcitool`/`l2ping`). ❌

## Installation 🛠️
## 🐧 Linux Setup (Kali/Ubuntu/Debian)
```bash
sudo apt update
# requirements 
sudo apt install bluez git

# (Recommended) Its work only root  permission

git clone https://github.com/thakur2309/BTSTORM.git
cd BTSTORM

# run script
sudo python bluetooth-jammer.py
```

#### On Arch Linux:
```bash
sudo pacman -Syu python bluez
```

#### Verify:
- python3 --version  # Should be 3.8+
- hcitool -h         # Should show help
- l2ping -h          # Should show help

### Step 3: Run the Tool
Always use **sudo**:sudo python3 bluetooth-jammer.py


- Enjoy the cool banner and credits! 🎨

2. **Scan for Devices**:
- Auto-scans nearby Bluetooth devices (30s max).

3. **Choose Attack Mode**:
- **All Devices**: Type `y` to flood all devices. 🌩️
- If connected (e.g., speaker to phone), auto-disconnect tries via `bluetoothctl`.
- L2ping flood (`-s 600 -f`) blocks reconnection.
- **Single Device**: Type `n`, enter MAC (e.g., `00:1A:7D:DA:71:13`) and name (e.g., `MySpeaker`).
- Validates MAC before attacking. 🔧

4. **Monitor & Stop**:
- Runs up to 1 hour or `Ctrl+C`.
- Logs: Green for wins, Red for errors (e.g., timeouts). 📊
- 
### Advanced Tips 💡
- **Force Disconnect**: Retries disconnect twice (restarts Bluetooth if needed).
- **Packet Tuning**: Edit `attack_device()`: Boost `-s 600` for stronger flood (use wisely). ⚡
- **Logging**: Save logs: `sudo python3 bluetooth-jammer.py > output.log`.
- **Troubleshooting**:
- "Operation not permitted": Use `sudo` or restart: `sudo systemctl restart bluetooth`.
- No devices: Ensure targets are discoverable (pairing mode). 🔍
- HCI0 down: Tool auto-fixes, or manual: `sudo hciconfig hci0 up`.


## ⚠️ Disclaimer
This tool is intended **only for educational and lawful use** on devices **you own** or have **explicit permission** to manage. The creator and contributors are **not responsible** for any misuse.  
Stay ethical — **Firewall Breaker** community promotes **learning & safety**, not harm.

---

👨‍💻 **Author**  
- Made with ❤️ by **thakur2309** 
- Name: **Alok Thakur**  
- YouTube: [🔥 Firewall Breaker](https://www.youtube.com/@FirewallBreaker09)

---
## 📌 Contact Me  

<a href="https://youtube.com/@firewallbreaker09">
  <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube">
</a>  
<br>  

<a href="https://github.com/thakur2309?tab=repositories">
  <img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>  
<br>  

<a href="https://whatsapp.com/channel/0029VbAiqVMKLaHjg5J1Nm2F">
  <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp Channel">
</a>

