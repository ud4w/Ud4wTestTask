
MANAGE=django-admin.py
SETTINGS=Ud4wTestTask.settings

test: check_noqa
    PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) test
    flake8 --exclude '*migrations*,Ud4wTestTask/settings/__init__.py' \
        --max-complexity=6 udaw_test Ud4wTestTask

check_noqa:
    bash check_noqa.sh

run:
    PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) runserver

syncdb:
    PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) syncdb --noinput

migrate:
    PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) migrate

collectstatic:
    PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) collectstatic --noinput
.PHONY: test syncdb migrate
