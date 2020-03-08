# Auto-redeem Weekly Free Games From Epic
*This script automatically redeems the weekly free games from Epic by interfacing with Chrome*

*How to set-up:*
1. Create a file named "accounts" in the same folder.
2. In the "accounts" file, 
follow this template:
    ```
    U0: (Email)
    P0: (Password)
    S0: (Enter secret 2FA here if applicable, else, leave blank)  
    U1: email@mymail.com
    P1: Password123
    S1: ASDPOSDPOIWMYSECRET2FACODE
    ```
3. Run epic.py in python (C:>python epic.py)
4. Your accounts should appear in the menu, if not repeat step 2

*Note: Only login works right now. Other capabilities are disabled and will be enabled in the future*