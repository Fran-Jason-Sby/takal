import base64
exec(base64.b64decode(b'IyEvdXNyL2Jpbi9weXRob24zCiMgLSotIGNvZGluZzogdXRmLTggLSotCgppbXBvcnQgcmVxdWVzdHMsYnM0LGpzb24sb3Msc3lzLHJhbmRvbSxkYXRldGltZSx0aW1lLHJlCnRyeToKCWltcG9ydCByaWNoCmV4Y2VwdCBJbXBvcnRFcnJvcjoKCW9zLnN5c3RlbSgncGlwIGluc3RhbGwgcmljaCcpCgl0aW1lLnNsZWVwKDEpCgl0cnk6CgkJaW1wb3J0IHJpY2gKCWV4Y2VwdCBJbXBvcnRFcnJvcjoKCQlleGl0KCdUaWRhayBEYXBhdCBNZW5naW5zdGFsbCBNb2R1bGUgcmljaCwgQ29iYSBJbnN0YWxsIE1hbnVhbCAocGlwIGluc3RhbGwgcmljaCknKQpmcm9tIHJpY2gudGFibGUgaW1wb3J0IFRhYmxlIGFzIG1lCmZyb20gcmljaC5jb25zb2xlIGltcG9ydCBDb25zb2xlIGFzIHNvbApmcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cCBhcyBzb3AKZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFRocmVhZFBvb2xFeGVjdXRvciBhcyB0cmVkCmZyb20gcmljaC5jb25zb2xlIGltcG9ydCBHcm91cCBhcyBncApmcm9tIHJpY2gucGFuZWwgaW1wb3J0IFBhbmVsIGFzIG5lbApmcm9tIHJpY2ggaW1wb3J0IHByaW50IGFzIGNldGFrCmZyb20gcmljaC5tYXJrZG93biBpbXBvcnQgTWFya2Rvd24gYXMgbWFyawpmcm9tIHJpY2guY29sdW1ucyBpbXBvcnQgQ29sdW1ucyBhcyBjb2wKIyBVQSBMSVNUCnRyeTp1Z2VuID0gb3BlbigndXNlci50eHQnLCdyJykucmVhZCgpLnNwbGl0bGluZXMoKQpleGNlcHQ6dWdlbiA9IFsnTW96aWxsYS81LjAgKExpbnV4OyBVOyBBbmRyb2lkIDIuMy40OyBwdC1wdDsgU29ueUVyaWNzc29uTFQxOGEgQnVpbGQvNC4wLjEuQS4wLjI2NikgQXBwbGVXZWJLaXQvNTMzLjEgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBNb2JpbGUgU2FmYXJpLzUzMy4xJywnTW96aWxsYS81LjAgKExpbnV4OyBVOyBBbmRyb2lkIDQuMi4xOyBydS1ydTsgOTkzMGkgQnVpbGQvSk9QNDBEKSBBcHBsZVdlYktpdC81MzQuMzAgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBNb2JpbGUgU2FmYXJpLzUzNC4zMCcsJ01vemlsbGEvNS4wIChMaW51eDsgVTsgQW5kcm9pZCAyLjMuNDsgcnUtcnU7IE1JRCBCdWlsZC9HUkoyMikgQXBwbGVXZWJLaXQvNTMzLjEgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBNb2JpbGUgU2FmYXJpLzUzMy4xJywnTW96aWxsYS81LjAgKExpbnV4OyBVOyBBbmRyb2lkIDQuMzsgZW4tdXM7IEFTVVNfVDAwSiBCdWlsZC9KU1MxNVEpIEFwcGxlV2ViS2l0LzUzNC4zMCAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIE1vYmlsZSBTYWZhcmkvNTM0LjMwJywnTW96aWxsYS81LjAgKExpbnV4OyBVOyBBbmRyb2lkIDQuMi4yOyBydS1ydTsgRmx5IElRNDQwNCBCdWlsZC9KRFEzOSkgQXBwbGVXZWJLaXQvNTM0LjMwIChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi80LjAgTW9iaWxlIFNhZmFyaS81MzQuMzAgWWFuZGV4U2VhcmNoLzcuMTYnXQp0cnk6dWdlbjIgPSBvcGVuKCd1c2VyMi50eHQnLCdyJykucmVhZCgpLnNwbGl0bGluZXMoKQpleGNlcHQ6dWdlbjIgPSBbJ01vemlsbGEvNS4wIChMaW51eDsgVTsgQW5kcm9pZCAyLjMuNDsgcHQtcHQ7IFNvbnlFcmljc3NvbkxUMThhIEJ1aWxkLzQuMC4xLkEuMC4yNjYpIEFwcGxlV2ViS2l0LzUzMy4xIChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi80LjAgTW9iaWxlIFNhZmFyaS81MzMuMScsJ01vemlsbGEvNS4wIChMaW51eDsgVTsgQW5kcm9pZCA0LjIuMTsgcnUtcnU7IDk5MzBpIEJ1aWxkL0pPUDQwRCkgQXBwbGVXZWJLaXQvNTM0LjMwIChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi80LjAgTW9iaWxlIFNhZmFyaS81MzQuMzAnLCdNb3ppbGxhLzUuMCAoTGludXg7IFU7IEFuZHJvaWQgMi4zLjQ7IHJ1LXJ1OyBNSUQgQnVpbGQvR1JKMjIpIEFwcGxlV2ViS2l0LzUzMy4xIChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi80LjAgTW9iaWxlIFNhZmFyaS81MzMuMScsJ01vemlsbGEvNS4wIChMaW51eDsgVTsgQW5kcm9pZCA0LjM7IGVuLXVzOyBBU1VTX1QwMEogQnVpbGQvSlNTMTVRKSBBcHBsZVdlYktpdC81MzQuMzAgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBNb2JpbGUgU2FmYXJpLzUzNC4zMCcsJ01vemlsbGEvNS4wIChMaW51eDsgVTsgQW5kcm9pZCA0LjIuMjsgcnUtcnU7IEZseSBJUTQ0MDQgQnVpbGQvSkRRMzkpIEFwcGxlV2ViS2l0LzUzNC4zMCAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIE1vYmlsZSBTYWZhcmkvNTM0LjMwIFlhbmRleFNlYXJjaC83LjE2J10KCiMgSU5ESUNBVElPTgppZCxpZDIsbG9vcCxvayxjcCxha3VuLG9wcmVrLG1ldGhvZCxsaXNlbnNpa3UsdGFwbGlrYXNpLHRva2Vua3UsdWlkLGxpc2Vuc2lrdW5pPSBbXSxbXSwwLDAsMCxbXSxbXSxbXSxbXSxbXSxbXSxbXSxbXQoKIyBDT0xPUlMKeCA9ICdcMzNbbScgIyBERUZBVUxUCmsgPSAnXDAzM1s5M20nICMgS1VOSU5HICsKaCA9ICdceDFiWzE7OTJtJyAjIEhJSkFVICsKaGggPSAnXDAzM1szMm0nICMgSElKQVUgLQp1ID0gJ1wwMzNbOTVtJyAjIFVOR1UKa2sgPSAnXDAzM1szM20nICMgS1VOSU5HIC0KYiA9ICdcMzNbMTs5Nm0nICMgQklSVSAtCnAgPSAnXHgxYlswOzM0bScgIyBCSVJVICsKIyBDb252ZXJ0ZXIgQnVsYW4KZGljID0geycxJzonSmFudWFyaScsJzInOidGZWJydWFyaScsJzMnOidNYXJldCcsJzQnOidBcHJpbCcsJzUnOidNZWknLCc2JzonSnVuaScsJzcnOidKdWxpJywnOCc6J0FndXN0dXMnLCc5JzonU2VwdGVtYmVyJywnMTAnOidPa3RvYmVyJywnMTEnOidOb3ZlbWJlcicsJzEyJzonRGVzZW1iZXInfQpkaWMyID0geycwMSc6J0phbnVhcmknLCcwMic6J0ZlYnJ1YXJpJywnMDMnOidNYXJldCcsJzA0JzonQXByaWwnLCcwNSc6J01laScsJzA2JzonSnVuaScsJzA3JzonSnVsaScsJzA4JzonQWd1c3R1cycsJzA5JzonU2VwdGVtYmVyJywnMTAnOidPa3RvYmVyJywnMTEnOidOb3ZlbWJlcicsJzEyJzonRGVzZW1iZXInfQp0Z2wgPSBkYXRldGltZS5kYXRldGltZS5ub3coKS5kYXkKYmxuID0gZGljWyhzdHIoZGF0ZXRpbWUuZGF0ZXRpbWUubm93KCkubW9udGgpKV0KdGhuID0gZGF0ZXRpbWUuZGF0ZXRpbWUubm93KCkueWVhcgpva2MgPSAnT0stJytzdHIodGdsKSsnLScrc3RyKGJsbikrJy0nK3N0cih0aG4pKycudHh0JwpjcGMgPSAnQ1AtJytzdHIodGdsKSsnLScrc3RyKGJsbikrJy0nK3N0cih0aG4pKycudHh0JwojIENMRUFSCmRlZiBjbGVhcigpOgoJb3Muc3lzdGVtKCdjbGVhcicpCiMgQkFDSwpkZWYgYmFjaygpOgoJbG9naW4oKQojIEJBTk5FUgpkZWYgYmFubmVyKCk6CgljbGVhcigpCgl3ZWwgPSAnIyBXRUxDT01FIFRPIEZBQ0VCT09LIDRNQkYgVE9PTFMgMjAyMicKCXdlbDIgPSBtYXJrKHdlbCwgc3R5bGU9J2N5YW4nKQoJc29sKCkucHJpbnQod2VsMikKCWF1PSdBVVRIT1IgICAgOiAgNDBSM0NcbkdJVEhVQiAgICA6ICBodHRwczovL2dpdGh1Yi5jb20vNDBSM0NcbldIQVRTQVBQICA6ICAwODc4NzI3Mzk4OTknCglwZW5nZW1iYW5nMT1uZWwoYXUsc3R5bGU9ImN5YW4iKQoJY2V0YWsobmVsKHBlbmdlbWJhbmcxLCB0aXRsZT0nSU5GT1JNQVNJIFBFTkdFTUJBTkcnKSkKCXdlbCA9ICcjIFNpbGFoa2FuIEJlbGkgTGlzZW5zaSBEdWx1IFVudHVrIE1lbGFuanV0a2FuJwoJd2VsMiA9IG1hcmsod2VsLCBzdHlsZT0nY3lhbicpCglzb2woKS5wcmludCh3ZWwyKQoJYWE9aW5wdXQoJ1vigKJdIEJlbGkgTGlzZW5zaSAgeSAvIHQgOiAnKQoJaWYgYWEgaW4gWyd5JywnWSddOgoJCW9zLnN5c3RlbSgneGRnLW9wZW4gaHR0cHM6Ly93YS5tZS82Mjg3ODcyNzM5ODk5JykKCWVsc2U6CgkJZXhpdCgpCgkJCgkKYmFubmVyKCkKCgo='))