import os


class Commend:

    @staticmethod
    def run(commend):
        stream = os.popen(commend)
        return stream.read()

    def disconnect(self):
        result = self.run('warp-cli disconnect')
        if result == 'Success':
            return True
        return False

    def account_type(self):
        result = self.run('warp-cli account')
        try:
            data = result.split('\n')
            result = data[0].split(': ')
            return result[1].lower()
        except:
            return False

    def connect(self):
        result = self.run('warp-cli connect')
        if result == 'Success':
            return True
        return False

    def status(self):
        output = self.run('warp-cli status')
        data = output.split('\n')
        result = data[0]
        if result == 'Success':
            status_message = data[1].split(':')[1]
            return status_message.strip()
        return False

    def set_mode(self, mode):
        result = self.run('warp-cli set-mode {}'.format(mode))
        if result == 'Success':
            return True
        return False

    def is_connected(self):
        status = self.status()
        if status == 'Connected':
            return True
        return False
