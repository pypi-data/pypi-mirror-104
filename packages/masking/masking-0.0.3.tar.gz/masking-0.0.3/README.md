This package contains a function '**maskstring**' to mask a given input string based on the index positions passed as arguments.

Project resources are available at https://github.com/sangram11/MASKING.git

Steps to install the package: -

$pip install masking

Example to show usage of this package: -
>>>import masking.maskstring as msk
>>>print(msk.maskstring('helo','*',2))

Output: -
>**l*

Alternatively you can supply multiple index values where you don't intent to mask.

>>>print(mask.maskstring('Password','*',0,7))

Output: -
>P******d