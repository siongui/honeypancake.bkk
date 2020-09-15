===============
How to Develope
===============

.. image:: https://travis-ci.org/siongui/honeypancake.bkk.svg?branch=master
    :target: https://travis-ci.org/siongui/honeypancake.bkk

.. See how to add travis ci image from https://raw.githubusercontent.com/demizer/go-rst/master/README.rst
   https://github.com/demizer/go-rst/commit/9651ab7b5acc997ea2751845af9f2d6efee825df

Development Tool: Pelican_ (static site generator written in Python)

Development Environment: `Ubuntu 20.04`_

Theme from `Bootstrap 4.5 Carousel Example`_


First-time Setup
----------------

1. Install git_ and pip_:

   .. code-block:: bash

     $ sudo apt-get install git
     $ sudo apt-get install python3-pip

2. Install language packages to add locale (English, Traditional Chinese in this
   example):

   .. code-block:: bash

     $ sudo apt-get install language-pack-en
     $ sudo apt-get install language-pack-zh-hant

3. git clone source code:

   .. code-block:: bash

     $ cd
     $ mkdir dev
     $ cd ~/dev/
     $ git clone https://github.com/siongui/honeypancake.bkk.git honeypancake.bkk

4. Install Python tools:

   .. code-block:: bash

     $ cd ~/dev/honeypancake.bkk/
     $ sudo pip install -r requirements.txt

5. Install Pelican `i18n_subsites`_ plugin:

   .. code-block:: bash

     $ cd ~/dev/honeypancake.bkk/
     $ make download

6. Generate CSS file:

   .. code-block:: bash

     $ cd ~/dev/honeypancake.bkk/
     $ make scss


Auto-deploy by `Travis CI`_
---------------------------

See `GitHub Pages Deployment - Travis CI`_.

First save your `personal access token`_ in `repository settings`_.

For Project Pages, the following is sample config:

.. code-block:: yaml

  deploy:
    provider: pages
    skip_cleanup: true
    github_token: $GITHUB_TOKEN
    local_dir: output
    on:
      branch: master


Daily Development
-----------------

.. code-block:: bash

    # start edit and develope
    $ cd ~/dev/honeypancake.bkk/
    # If something changes, re-generate the website:
    $ make html
    # start dev server
    $ make
    # open your browser and preview the website at http://localhost:8000/


References
----------

.. [1] `Deploy Website by Pelican, Travis CI, and GitHub Pages <https://siongui.github.io/2016/01/05/deploy-website-by-pelican-travis-ci-github-pages/>`_

.. [2] JINJA_FILTERS in `Settings — Pelican documentation <http://docs.getpelican.com/en/latest/settings.html>`_

       `Jinja custom filters documentation <http://jinja.pocoo.org/docs/dev/api/#custom-filters>`_

.. [3] `𝒉𝒐𝒏𝒆𝒚𝒑𝒂𝒏𝒄𝒂𝒌𝒆.𝒃𝒌𝒌 (@honeypancake.bkk) <https://www.instagram.com/honeypancake.bkk/>`_


.. _Pelican: http://blog.getpelican.com/
.. _Ubuntu 20.04: http://releases.ubuntu.com/20.04/
.. _UNLICENSE: http://unlicense.org/
.. _git: https://git-scm.com/
.. _pip: https://pypi.python.org/pypi/pip
.. _i18n_subsites: https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites
.. _Travis CI: https://travis-ci.org/
.. _GitHub Pages Deployment - Travis CI: https://docs.travis-ci.com/user/deployment/pages/
.. _personal access token: https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
.. _repository settings: https://docs.travis-ci.com/user/environment-variables#Defining-Variables-in-Repository-Settings
.. _Google Adsense: https://www.google.com/search?q=Google+AdSense
.. _Bootstrap 4.5 Carousel Example: https://getbootstrap.com/docs/4.5/examples/carousel/
