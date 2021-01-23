Name:       mls-austria
Version:    1.0.0
Release:    1
Summary:    MLS data for Austria
License:    Public Domain
BuildRequires: geoclue-provider-mlsdb-tool
BuildRequires: curl
BuildArch:  noarch
Source0:    https://d2koia3g127518.cloudfront.net/export/MLS-full-cell-export-2021-01-23T000000.csv.gz

%description

%prep
curl https://d2koia3g127518.cloudfront.net/export/MLS-full-cell-export-2021-01-23T000000.csv.gz -o mls-full.csv.gz
gunzip mls-full.csv.gz

%build
geoclue-mlsdb-tool -c Austria mls-full.csv

%install
mkdir -p %{buildroot}/usr/share/geoclue-provider-mlsdb/
cp -r {1,2,3,4,5,6,7,8,9}/ %{buildroot}/usr/share/geoclue-provider-mlsdb/

%files
/usr/share/geoclue-provider-mlsdb/

%changelog
# Initial version
