
This is on how to make an RPM of Mozilla Location Service on your SailfishOS device for improving GPS functionality.

# How to use

 - Install `rpmbuild` on your SailfishOS: https://talk.maemo.org/showthread.php?t=92963
 - If you donn't live in Austria, change the country in `mls-austria.spec`
 - `scp mls-austria.spec nemo@a.b.c.d:/tmp/`
 - `ssh nemo@a.b.c.d`
 - `devel-su rpmbuild -ba -v /tmp/mls-austria.spec`

Note that it will fail, if you don't have enough space.

# References

- Mozilla's location service: https://location.services.mozilla.com/downloads
- Sailfish's forum entry: https://forum.sailfishos.org/t/any-replacement-plan-for-mozilla-location-service/4190/
- MLS export as RPM per country: https://openrepos.net/user/15461/programs
