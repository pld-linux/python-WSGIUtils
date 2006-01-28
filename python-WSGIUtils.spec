Summary:	Collection of libraries for use in a WSGI environnmen
Name:		python-WSGIUtils
Version:	0.7
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://cheeseshop.python.org/packages/source/W/WSGIUtils/WSGIUtils-%{version}.tar.gz
# Source0-md5:	80656ce771bb33eb8ad502c3b674b1fc
URL:		http://kid.lesscode.org/
BuildRequires:	python-devel
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WSGIUtils is a package of standalone utility libraries that ease the
development of simple WSGI programs. The package is divided into two main
components which can be used individualy or in combination:

- wsgiServer is a multi-threaded WSGI web server based on SimpleHTTPServer
- wsgiAdaptor is a simple WSGI application that provides basic authentication,
  signed cookies and persistent sessions

%prep
%setup -q -n WSGIUtils-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/wsgiutils*
%{py_sitescriptdir}/WSGIUtils*