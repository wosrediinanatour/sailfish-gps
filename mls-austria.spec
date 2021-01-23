Name:       mls-austria
Version:    1.0.0
Release:    1
Summary:    MLS data for Austria
License:    Public Domain
BuildRequires: geoclue-provider-mlsdb-tool
BuildRequires: curl
BuildArch:  noarch

%description

%prep
curl "https://d2koia3g127518.cloudfront.net/export/MLS-full-cell-export-$(date -I --date="yesterday").csv.gz" | gunzip - > MLS-full-cell-export.csv

%build
geoclue-mlsdb-tool -c Austria MLS-full-cell-export.csv
rm MLS-full-cell-export.csv

%install
mkdir -p %{buildroot}/usr/share/geoclue-provider-mlsdb/
cp -r {1,2,3,4,5,6,7,8,9}/ %{buildroot}/usr/share/geoclue-provider-mlsdb/

%files
/usr/share/geoclue-provider-mlsdb/

%changelog
# Initial version
