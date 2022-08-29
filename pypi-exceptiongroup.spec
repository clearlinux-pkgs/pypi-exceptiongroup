#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-exceptiongroup
Version  : 1.0.0rc9
Release  : 14
URL      : https://files.pythonhosted.org/packages/cb/b2/ca0513bb83e236707e22218d1e52d5f5b38b608653d385edb3fb3a03d35f/exceptiongroup-1.0.0rc9.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/b2/ca0513bb83e236707e22218d1e52d5f5b38b608653d385edb3fb3a03d35f/exceptiongroup-1.0.0rc9.tar.gz
Summary  : Backport of PEP 654 (exception groups)
Group    : Development/Tools
License  : MIT
Requires: pypi-exceptiongroup-license = %{version}-%{release}
Requires: pypi-exceptiongroup-python = %{version}-%{release}
Requires: pypi-exceptiongroup-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_scm)

%description
.. image:: https://github.com/agronholm/exceptiongroup/actions/workflows/test.yml/badge.svg
:target: https://github.com/agronholm/exceptiongroup/actions/workflows/test.yml
:alt: Build Status
.. image:: https://coveralls.io/repos/github/agronholm/exceptiongroup/badge.svg?branch=main
:target: https://coveralls.io/github/agronholm/exceptiongroup?branch=main
:alt: Code Coverage

%package license
Summary: license components for the pypi-exceptiongroup package.
Group: Default

%description license
license components for the pypi-exceptiongroup package.


%package python
Summary: python components for the pypi-exceptiongroup package.
Group: Default
Requires: pypi-exceptiongroup-python3 = %{version}-%{release}

%description python
python components for the pypi-exceptiongroup package.


%package python3
Summary: python3 components for the pypi-exceptiongroup package.
Group: Default
Requires: python3-core
Provides: pypi(exceptiongroup)

%description python3
python3 components for the pypi-exceptiongroup package.


%prep
%setup -q -n exceptiongroup-1.0.0rc9
cd %{_builddir}/exceptiongroup-1.0.0rc9
pushd ..
cp -a exceptiongroup-1.0.0rc9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661792397
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-exceptiongroup
cp %{_builddir}/exceptiongroup-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-exceptiongroup/084d0531a95caca443a618b31f06897d65dcb2e8 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-exceptiongroup/084d0531a95caca443a618b31f06897d65dcb2e8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
