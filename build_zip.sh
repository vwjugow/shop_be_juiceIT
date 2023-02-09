#!/bin/bash

OUTPUT_ZIP="./flask-app.zip"
ARCHIVE_TMP="./lambda-bundle-tmp.zip"

addToZip() {
    echo "params: ${@}"
    zip -r9 "$ARCHIVE_TMP" \
            --exclude pipenv-2018.11.26.dist-info/\* \
            --exclude virtualenv-16.7.9.dist-info/\* \
            --exclude virtualenv_clone-0.5.3.dist-info/\* \
            --exclude virtualenv_support/\* \
            --exclude pip-9.0.3.dist-info/\* \
            --exclude setuptools-38.4.0.dist-info/\* \
            --exclude setuptools/\* \
            --exclude pipenv/\* \
            --exclude pip/\* \
            --exclude easy_install\* \
            --exclude ./\*.pyc \
            -- "${@}"
}

addDependencies() {
    local packages_dir=()
    packages_dir=($(python3 -c "import site; print(' '.join(site.getsitepackages()))"))
    echo ${packages_dir}
    for (( i=0; i<${#packages_dir[@]}; i++ )); do
        if [[ -d "${packages_dir[$i]}" ]]; then
            cd "${packages_dir[$i]}"
            addToZip -- *
            cd -
        fi
    done
}

rm -f ${ARCHIVE_TMP} ${OUTPUT_ZIP}
addToZip project/ ./*.py
echo "project done"
addDependencies
echo "dep done"
mv ${ARCHIVE_TMP} ${OUTPUT_ZIP}
