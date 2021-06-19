#!/bin/bash

GIT=$(which git)
RSYNC=$(which rsync)
REPO="Repositorio GIT"
TMPDIR=$(mktemp -d "/tmp/git_.XXXXX")
BRANCH="$2"
TAG="$3"
OWNER="$4"
DSTDIR="$5"

if [ -z $2 ];then
cat <<EOF
usage: $0 [repo] [branch] [tag] [usuario] [local]

EOF
        exit 1
fi

if ! getent passwd $OWNER >/dev/null 2>&1;then
    echo "Usuario informado nao existe"
    exit 1
fi

if [ ! -d $DSTDIR ];then
        echo "O destino nao eh um diretorio"
else
        ($GIT clone -b $BRANCH $REPO $TMPDIR >/dev/null 2>&1 || echo "Falha ao clonar o repositorio[$1], verificar o servidor ou o /tmp") && \
    (cd $TMPDIR; git checkout ${TAG} 2>&1 | grep '^HEAD') && \
        (chown -R $OWNER:$OWNER $TMPDIR) && \
        (find $TMPDIR -type d -exec chmod 755 {} \;) && \
        (find $TMPDIR -type f -exec chmod 644 {} \;) && \
        (cd $TMPDIR && $RSYNC -a --exclude '*.git' . $DSTDIR)
fi

if [ -d ${TMPDIR} ];then
        rm -rf ${TMPDIR}
fi
