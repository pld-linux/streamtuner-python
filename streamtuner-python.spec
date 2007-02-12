Summary:	Plugin for streamtuner providing an embedded Python interpreter
Summary(pl.UTF-8):	Wtyczka dla streamtunera dostarczająca wbudowany interpreter Pythona
Name:		streamtuner-python
Version:	0.1.2
Release:	1
License:	Free
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/streamtuner/%{name}-%{version}.tar.gz
# Source0-md5:	018867f35a50dca2bbdae5ef58926ca8
URL:		http://www.nongnu.org/streamtuner/
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	python-devel >= 2.2
BuildRequires:	streamtuner-devel >= 0.12.0
Requires:	streamtuner >= 0.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin for streamtuner providing an embedded Python interpreter.

%description -l pl.UTF-8
Wtyczka dla streamtunera dostarczająca wbudowany interpreter Pythona.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/streamtuner/plugins/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/streamtuner/plugins/*.so
%{_datadir}/%{name}
