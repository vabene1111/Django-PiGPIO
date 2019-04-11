// GPIO Output Block - Takes a pin and number to set the pins state
Blockly.Blocks['gpio_output'] = {
    init: function () {
        this.appendValueInput("pin")
            .setCheck(["Number", "Array"])
            .appendField("output GPIO pin(s)");
        this.appendValueInput("state")
            .setCheck("Number")
            .setAlign(Blockly.ALIGN_RIGHT)
            .appendField("state");
        this.setInputsInline(false);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(65);
        this.setTooltip("Sets state of given GPIO Pin");
        this.setHelpUrl(docUrls.block_gpio_output);
    }
};

Blockly.Python['gpio_output'] = function (block) {
    var value_pin = Blockly.Python.valueToCode(block, 'pin', Blockly.Python.ORDER_ATOMIC);
    var value_state = Blockly.Python.valueToCode(block, 'state', Blockly.Python.ORDER_ATOMIC);

    Blockly.Python.definitions_['from_pigpio_helper_import_raspi'] = 'from PiGPIO.helper import raspi';

    return 'raspi.setup_pin(' + value_pin + ', 1)\nraspi.set_output(' + value_pin + ',' + value_state + ')\n';
};

// GPIO Input Block
Blockly.Blocks['gpio_input'] = {
    init: function () {
        this.appendValueInput("pin")
            .setCheck("Number")
            .appendField("read GPIO pin");
        this.setInputsInline(false);
        this.setOutput(true, "Number");
        this.setColour(65);
        this.setTooltip("Reads state of given GPIO Pin");
        this.setHelpUrl(docUrls.block_gpio_input);
    }
};

Blockly.Python['gpio_input'] = function (block) {
    let value_pin = Blockly.Python.valueToCode(block, 'pin', Blockly.Python.ORDER_ATOMIC);

    Blockly.Python.definitions_['from_pigpio_helper_import_raspi'] = 'from PiGPIO.helper import raspi';

    let code = 'raspi.get_input(' + value_pin + ')';

    return [code, Blockly.Python.ORDER_NONE];
};

// Sleep Block - pauses execution for given amount of milliseconds
Blockly.Blocks['sleep'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("sleep (seconds)")
            .appendField(new Blockly.FieldNumber(0, 0), "sleep");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(65);
        this.setTooltip("Halts execution for given amount of seconds");
        this.setHelpUrl(docUrls.block_sleep);
    }
};

Blockly.Python['sleep'] = function (block) {
    let number_sleep = block.getFieldValue('sleep');

    Blockly.Python.definitions_['from_time_import_sleep'] = 'from time import sleep';

    return 'sleep(' + number_sleep + ')\n';
};

// Sets Board Mode
Blockly.Blocks['gpio_mode'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("GPIO Board Mode")
            .appendField(new Blockly.FieldDropdown([["Board", "0"], ["BCM", "1"]]), "gpio_mode");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(65);
        this.setTooltip("Sets mode. If unsure leave at Board.");
        this.setHelpUrl(docUrls.block_gpio_mode);
    }
};

Blockly.Python['gpio_mode'] = function (block) {
    let dropdown_gpio_mode = block.getFieldValue('gpio_mode');

    Blockly.Python.definitions_['from_pigpio_helper_import_raspi'] = 'from PiGPIO.helper import raspi';

    return 'raspi.set_mode(' + dropdown_gpio_mode + ');\n';
};

// Logs to DB for output on run page
Blockly.Blocks['log'] = {
    init: function () {
        this.appendValueInput("data")
            .setCheck(null)
            .appendField("log");
        this.setInputsInline(false);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(65);
        this.setTooltip("Logs given input");
        this.setHelpUrl(docUrls.block_log);
    }
};

Blockly.Python['log'] = function (block) {
    let value_data = Blockly.Python.valueToCode(block, 'data', Blockly.Python.ORDER_ATOMIC);

    Blockly.Python.definitions_['from_pigpio_helper_import_raspi'] = 'from PiGPIO.helper import raspi';

    return 'raspi.log( "LOG: " + str(' + value_data + '))\n';
};

// Debug block - if block is added and checked debug variable is set at beginning of script
Blockly.Blocks['debug'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("debug mode ")
            .appendField(new Blockly.FieldCheckbox("TRUE"), "debug_mode");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(65);
        this.setTooltip("activate this block to get more verbose logging");
        this.setHelpUrl(docUrls.block_debug);
    }
};

Blockly.Python['debug'] = function (block) {
    let checkbox_debug_mode = block.getFieldValue('debug_mode') == 'TRUE';

    Blockly.Python.definitions_['from_pigpio_helper_import_raspi'] = 'from PiGPIO.helper import raspi';

    if (checkbox_debug_mode) {
        Blockly.Python.definitions_['debug_mode_true'] = 'raspi.DEBUG = True';
    } else {
        Blockly.Python.definitions_['debug_mode_true'] = 'raspi.DEBUG = False';
    }

    return '';
};