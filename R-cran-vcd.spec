%define		fversion	%(echo %{version} |tr r -)
%define		modulename	vcd
Summary:	Visualizing Categorical Data
Name:		R-cran-%{modulename}
Version:	1.3r1
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	3529759583680bd45f8b4ddf3252dc39
URL:		http://cran.fhcrc.org/web/packages/vcd/index.html
BuildRequires:	R >= 2.8.1
BuildRequires:	R-cran-colorspace
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
Requires:	R-cran-colorspace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Visualization techniques, data sets, summary and inference procedures
aimed particularly at categorical data. Special emphasis is given to
highly extensible grid graphics. The package was inspired by the book
"Visualizing Categorical Data" by Michael Friendly.

%prep
%setup -q -c

%build
R CMD build %{modulename} --no-build-vignettes

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
