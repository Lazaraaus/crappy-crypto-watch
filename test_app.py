import cbpro

auth_client = cbpro.AuthenticatedClient('9NzFt0edVIpcCPE5gQMeH/+UQ1oPR2JmnZUNajiJqyifQJlpJ56LFGmENjwZGtfB9Iho4Z0GKg1gNrKH7FE3pw==',
										 b64secret, 'c0xsw4in')
title = 'CoinView'

account = auth_client.get_account('c09599217904c2263eda0434a625d5e3')

print(account)

