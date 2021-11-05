from .remote import RemoteProject


class Laravel(RemoteProject):
    major_version = 'v8'
    remote = 'https://github.com/laravel/laravel.git'

    @property
    def platformify(self):
        return super(Laravel, self).platformify + [
            'cd {0} && composer require platformsh/laravel-bridge'.format(self.builddir) + self.composer_defaults(),
        ]
