class UsageTranslator:
    def __init__(self, from_type, to_type, translations):
        self.from_type = from_type
        self.to_type = to_type
        self.translations = self.__process_translations__(translations, from_type)

    def __process_translations__(self, translations, from_type):
        keyed_translations = {}
        for command in translations['commands']:
            if from_type in command:
                if isinstance(command[from_type], list):
                    for variation in command[from_type]:
                        keyed_translations[variation] = command
                else:
                    keyed_translations[command[from_type]] = command
        return keyed_translations

    def __usage_from_to__(self, from_args, to_args, width=None, indent=0):
        return '{indent}{from_cmd} {from_args} => {to_cmd} {to_args}'.format(
            from_args=from_args if width is None else from_args.ljust(width),
            to_args=to_args,
            from_cmd=self.from_type,
            to_cmd=self.to_type,
            indent=' ' * indent,
        )

    def __get_usage__(self, cmd_translation, args_key):
        usage_key = '{to_cmd}_usage'.format(to_cmd=self.to_type)
        is_custom_usage = usage_key in cmd_translation

        if is_custom_usage:
            usage = cmd_translation[usage_key]
        elif self.to_type in cmd_translation:
            usage = cmd_translation[self.to_type]
            if isinstance(usage, list):
                usage = usage[0]
        else:
            return None

        if isinstance(usage, dict):
            longest_left = max(usage.keys(), key=len)
            return 'Translates as:\n' + '\n'.join(
                self.__usage_from_to__(
                    from_args=key,
                    to_args=value,
                    width=len(longest_left),
                    indent=4,
                )
                for key, value in usage.iteritems()
            )
        elif isinstance(usage, list):
            return 'Multiple translations found:\n    ' + '\n    '.join(
                '{to_cmd} {to_args}'.format(
                    to_args=to_args,
                    to_cmd=self.to_type
                ) for to_args in usage)
        elif is_custom_usage:
            return usage
        else:
            return '{to_cmd} {to_args}'.format(to_cmd=self.to_type, to_args=usage)

    def lookup_usage(self, args):
        for i in range(len(args), 0, -1):
            arg_string = ' '.join(args[:i])
            if arg_string in self.translations:
                header = '{from_type} {args}:'.format(args=arg_string,
                                                     from_type=self.from_type)
                usage = self.__get_usage__(self.translations[arg_string], arg_string)
                if usage is not None:
                    return '\n'.join((
                        header,
                        '=' * len(header),
                        usage
                    ))
                else:
                    return None
