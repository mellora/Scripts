# Variables for script
$HOSTNAME='10.1.1.11'
$NET_SHARES=[ordered]@{
  'Z:'='/mnt/Store/Data/Documents';
  'Y:'='/mnt/Store/Data/Music';
  'X:'='/mnt/Store/Data/Pictures';
  'W:'='/mnt/Store/Data/Videos';
  'V:'='/mnt/Tank/ISO';
  'U:'='/mnt/Store/Backups';
}

# Makes sure the shares are unmounted for script's sake
umount.exe -f -a

# Loops through the NET_SHARES Hash Table to mount the NFS shares
foreach ( $SHARE in $NET_SHARES.GetEnumerator() ){
  mount.exe -o nolock ${HOSTNAME}:$($SHARE.Value) $($SHARE.Name)
}
