
This is on how to make an RPM of Mozilla Location Service on your SailfishOS device for improving GPS functionality.

# Simple usage

 - Install `rpmbuild` on your SailfishOS: https://talk.maemo.org/showthread.php?t=92963
 - On your mobile: `cd /tmp/; curl -O https://raw.githubusercontent.com/wosrediinanatour/sailfish-gps/master/mls-austria.spec`
 - If you donn't live in Austria, change the country in via `vi mls-austria.spec` (type `i` for insert, edit the country, type `ESC`, type `:qw`)
 - Build RPM: `devel-su rpmbuild -ba -v /tmp/mls-austria.spec`
 - RPM is in `/root/rpmbuild/RPMS/noarch/mls-austria-1.0.0-1.noarch.rpm`
 - Download it via  `scp nemo@a.b.c.d:/root/rpmbuild/RPMS/noarch/mls-austria-1.0.0-1.noarch.rpm .`


# How to use via cloning this repo

 - Install `rpmbuild` on your SailfishOS: https://talk.maemo.org/showthread.php?t=92963
 - Clone the repo: `git clone https://github.com/wosrediinanatour/sailfish-gps.git`
 - If you donn't live in Austria, change the country in `mls-austria.spec`
 - `scp mls-austria.spec nemo@a.b.c.d:/tmp/`
 - `ssh nemo@a.b.c.d`
 - Build RPM: `devel-su rpmbuild -ba -v /tmp/mls-austria.spec`
 - RPM is in `/root/rpmbuild/RPMS/noarch/mls-austria-1.0.0-1.noarch.rpm`
 - Download it via  `scp nemo@a.b.c.d:/root/rpmbuild/RPMS/noarch/mls-austria-1.0.0-1.noarch.rpm .`

Note that it will fail, if you don't have enough space.

# References

- Mozilla's location service: https://location.services.mozilla.com/downloads
- Sailfish's forum entry: https://forum.sailfishos.org/t/any-replacement-plan-for-mozilla-location-service/4190/
- MLS export as RPM per country: https://openrepos.net/user/15461/programs
