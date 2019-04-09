// GPIO Output Block - Takes a pin and number to set the pins state
Blockly.Blocks['gpio_output'] = {
    init: function () {
        this.appendValueInput("pin")
            .setCheck("Number")
            .appendField("output GPIO pin");
        this.appendValueInput("state")
            .setCheck("Number")
            .setAlign(Blockly.ALIGN_RIGHT)
            .appendField("state");
        this.setInputsInline(false);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(65);
        this.setTooltip("Sets state of given GPIO Pin");
        this.setHelpUrl("");
    }
};

Blockly.Python['gpio_output'] = function (block) {
    var value_pin = Blockly.Python.valueToCode(block, 'pin', Blockly.Python.ORDER_ATOMIC);
    var value_state = Blockly.Python.valueToCode(block, 'state', Blockly.Python.ORDER_ATOMIC);

    Blockly.Python.definitions_['from_pigpio_helper_import_raspi'] = 'from PiGPIO.helper import raspi';

    return 'raspi.setup_pin(' + value_pin + ', 1)\nraspi.set_output(' + value_pin + ',' + value_state + ')\n';
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
        this.setTooltip("pauses execution for given seconds");
        this.setHelpUrl("");
    }
};

Blockly.Python['sleep'] = function (block) {
    var number_sleep = block.getFieldValue('sleep');

    Blockly.Python.definitions_['from_time_import_sleep'] = 'from time import sleep';

    return 'sleep(' + number_sleep + ')\n';
};