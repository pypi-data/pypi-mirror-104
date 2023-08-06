Flask-CKFinder3
===============

Flask CKFinder3 connector.

Installation
------------

::

   pip install Flask-CKFinder3

Running the example
-------------------

::

   git clone https://gitlab.com/aristofor/flask-ckfinder3.git
   cd flask-ckfinder3
   FLASK_APP=example.app flask run

Limitations
-----------

Supported backend : local file system

Proxy command not implemented.

Configuration
-------------

Required options

+-----------------------------------+---------------------------------------+
| ``CKFINDER_QUICKUPLOAD_DIR``      | Directory for quick upload            |
+-----------------------------------+---------------------------------------+
| ``CKFINDER_QUICKUPLOAD_ENDPOINT`` | Route name for quick upload           |
+-----------------------------------+---------------------------------------+
| ``CKFINDER_RESOURCE_TYPES``       | Resources list (see bellow)           |
+-----------------------------------+---------------------------------------+

Resources declaration

::

   CKFINDER_RESOURCE_TYPES = [
           dict(
               name='<unique resource name>',
               endpoint='<flask endpoint to use in url_for>',
               allowedExtensions='<comma separated list of extensions>',
               directory='<path to resource>',
               deniedExtensions='<denied extensions, default: None>',
               acl=<ACL flags, default: 1023>
           ),
           ...
       ]

Optionnal configuration

+-----------------------------------+---------------------------------------+
| ``CKFINDER_LICENSE_NAME``         | CKFinder license name                 |
+-----------------------------------+---------------------------------------+
| ``CKFINDER_LICENCE_KEY``          | CKFinder license code                 |
+-----------------------------------+---------------------------------------+
| ``CKFINDER_THUMBS``               | Thumbnails sizes. default:            |
|                                   | ``("150x150","300x300","500x500")``   |
+-----------------------------------+---------------------------------------+
| ``CKFINDER_THUMBNAIL_DIR``        | Thumbnails directory, required for    |
|                                   | caching                               |
+-----------------------------------+---------------------------------------+
| ``CKFINDER_THUMBNAIL_MAXFILES``   | Files to keep in thumbnail cache.     |
|                                   | default: ``200``                      |
+-----------------------------------+---------------------------------------+
| ``CKFINDER_THUMBNAIL_THRESHOLD``  | Thumbnail gc probability. default:    |
|                                   | ``1/20``                              |
+-----------------------------------+---------------------------------------+
| ``CKFINDER_UPLOADMAXSIZE``        | Maximum upload size                   |
+-----------------------------------+---------------------------------------+
| ``CKFINDER_UPLOADCHECKIMAGES``    | Check size before upload              |
+-----------------------------------+---------------------------------------+
| ``CKFINDER_IMAGES_SIZES``         | Resize presets dict                   |
+-----------------------------------+---------------------------------------+


Links
-----

`CKFinder page <https://ckeditor.com/ckfinder/>`_

`CKFinder command reference <https://ckeditor.com/docs/ckfinder/ckfinder3-php/commands.html>`_

History
-------

0.1.1 (2021-05-06)
~~~~~~~~~~~~~~~~~~

-  Edit image implemented
-  Resize image implemented
-  Fixed: thumbnailing non-RGB image

0.1.0 (2021-04-30)
~~~~~~~~~~~~~~~~~~

-  First release on PyPI
