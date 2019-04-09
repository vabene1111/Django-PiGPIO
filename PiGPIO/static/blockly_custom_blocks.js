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
        this.setColour(150);
        this.setTooltip("Sets state of given GPIO Pin");
        this.setHelpUrl("");
    }
};

Blockly.Python['gpio_output'] = function (block) {
    var value_pin = Blockly.Python.valueToCode(block, 'pin', Blockly.Python.ORDER_ATOMIC);
    var value_state = Blockly.Python.valueToCode(block, 'state', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble Python into code variable.
    var code = 'GPIO.out(' + value_pin + ',' + value_state + ')\n';
    return code;
};