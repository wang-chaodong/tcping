%global debug_package %{nil}

Name:		tcping         
Version:        1.0
Release:        1%{?dist}
Summary:        端口检测工具。

License:        MulanPSL-2.0
URL:            www.delcare.cn
Source0:        https://github.com/wang-chaodong/tcping/archive/refs/tags/v%{version}.tar.gz

BuildArch: noarch

BuildRequires:  python3
Requires:       python3

%description
端口检测工具。

%prep
%autosetup

%build

%install
install -Dpm 755 tcping.py %{buildroot}%{_bindir}/tcping

%files
%license LICENSE
%doc README.md
%{_bindir}/tcping

%changelog
* Thu Jun 25 2026 超东<479961270@qq.com> - v1.0-1
- init for rpm.
