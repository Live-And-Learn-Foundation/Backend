from django.http import JsonResponse


def jwks_view(request):
    return JsonResponse({
        "keys": [
            {
                "kty": "RSA",
                "kid": "b934ef091e942910fe806339982ba80c93581ccd37890ccfa0f0568cdcbdd235",
                "use": "sig",
                "alg": "RS256",
                "n": "0PGK60hs2dCPjOKHK7vC8gz9E3kKOmFBMYXAoG0IWui1cOIpeH4o3CcA9j7v_NL1_54yJiVpKNEPwSTQzBvKUsvoWjRN83Iq7kBNPj6Q7_GYuzTy9m_rLZwmSZF5vw0iOU58Nma99-YFEreICnu9YphKX3qv7fdK0pGwk3R7EPSTE-l5zksIHSYCKHOhs--rg8hQKWVZD_eWSplqyRCktDYybmvlf_FTGbEI-dCx4mR5db5wvHCZSEr5gTqrdjxkt3INj_UOr3kiKWE1N3PmZ4JRcjHCRSOqKAr78Nq1aeQthXPvFWOZhufgFmMWnkkcMPzroT1SB1WAo5sG_MvQnQ",
                "e": "AQAB"
            }
        ]
    })
