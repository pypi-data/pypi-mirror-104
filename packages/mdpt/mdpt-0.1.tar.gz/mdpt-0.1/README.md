**mdmt**\
is a protocol for data transfer

project include:\
_ request generator\
_ request parser\
_ simple socket server / client

\
\
request:

    mdpt/0.1
    length: ##
    ##meta##
    
    -
    ##data##

\
\
generating:

    mdpt(meta).g(data)
\
parsing data:

    mdpt().u(pkg)
\
parsing metadata:

    mdpt().m(pkg)
\
parsing data length:

    mdpt().l(pkg, include_meta, minus)
include_meta: bool if True returns length with metadata
minus: int subtracts minus value
