# dna.py Documentation

## Running script from terminal

```
sudo python dna.py -c
```

## DNA service

### Installing service

Copy dna.service to `/lib/systemd/system`

Set permissions:
```
sudo chmod 644 /lib/systemd/system/dna.service
```

Configure systemd
```
sudo systemctl daemon-reload
sudo systemctl enable dna.service
```

Service will now run on startup.

### Start/stop service

```
sudo systemctl start dna
sudo systemctl stop dna
```
