
###############################
'''  Logging                '''
###############################

LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'formatters': {
   'verbose': {
      'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    },
    'simple': {
      'format': '%(levelname)s %(message)s'
    }
  },
  'handlers': {
    'null': {
        'level': 'DEBUG',
        'class': 'logging.NullHandler',
    },
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
      'formatter': 'simple'
    },
    'debug_file': {
      'level': 'DEBUG',
      'class': 'logging.handlers.RotatingFileHandler',
      'formatter': 'verbose',
      'filename': 'snowshoe.debug.log',
      'maxBytes': 1024,
      'backupCount': 3
    },
    'error_file': {
      'level': 'ERROR',
      'class': 'logging.handlers.RotatingFileHandler',
      'formatter': 'verbose',
      'filename': 'snowshoe.error.log',
      'maxBytes': 1024,
      'backupCount': 3
    },
    'request_file': {
      'level': 'ERROR',
      'class': 'logging.handlers.RotatingFileHandler',
      'formatter': 'verbose',
      'filename': 'snowshoe.request.log',
      'maxBytes': 1024,
      'backupCount': 3
    },
    'security_file': {
      'level': 'ERROR',
      'class': 'logging.handlers.RotatingFileHandler',
      'formatter': 'verbose',
      'filename': 'snowshoe.security.log',
      'maxBytes': 1024,
      'backupCount': 3
    }
  },
  'loggers': {
    'default': {
      'handlers': ['debug_file','error_file','request_file','security_file'],
      'level': 'DEBUG',
      'propagate': True,
    }
  }
}
