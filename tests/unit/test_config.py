import os

from shulkr.config import Config, init_config


class TestConfig:
	def test_save_opens_config_file_for_writing(self, mocker):
		# 1. Create a new configuration
		config = Config('foo')

		# 2. Mock open()
		open_ = mocker.patch('shulkr.config.open')

		# 3. Try to save the configuration to the disk
		config.save()

		# 4. Make sure open() was called currectly
		config_path = os.path.join('foo', '.shulkr')
		open_.assert_called_once_with(config_path, 'w+')


def test_init_config_creates_new_configuration_with_provided_arguments_if_config_file_is_not_found(mocker):
	# 1. Spy on Config constructor
	Config_ = mocker.patch('shulkr.config.Config')

	# 2. Patch os.path.exists to return False
	mocker.patch('shulkr.config.os.path.exists', return_value=False)

	# 3. Call init_config
	init_config('foo', 'mojang')

	# 4. The Config constructor should have been called with the specified
	# path and mappings
	Config_.assert_called_once_with('foo', 'mojang')


def test_init_config_loads_existing_config_if_config_file_is_found(mocker):
	# 1. Stub out the Config constructor
	Config_ = mocker.patch('shulkr.config.Config')

	# 2. Add a fake config
	# 2a. Patch os.path.exists to return True
	mocker.patch('shulkr.config.os.path.exists', return_value=True)

	# 2b. Stub out open()
	mocker.patch('shulkr.config.open')

	# 2c. Patch toml.load to return a dummy config file
	raw_config = {
		'mappings': 'yarn'
	}
	mocker.patch('shulkr.config.toml.load', return_value=raw_config)

	# 3. Call init_config
	init_config('foo', 'mojang')

	# 4. The Config constructor should have been called with the path and
	# mappings from the existing config
	Config_.assert_called_once_with(repo_path='foo', mappings='yarn')