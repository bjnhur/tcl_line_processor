create_clock -period 10.0 \
    -waveform {0 5} \
    [get_ports {clk}]

set_input_delay -max 2.5 -clock [ \
    get_clocks clk] {              





        
    [get_ports {\  
        data_in3 { 
            test
        }
        }
        ]
    [get_ports {data_in2 \         
    }]
}



set_input_delay -max 2.5 -clock [get_clocks clk] {              
    [get_ports {\  
        data_in3 { 
            test
        }
        }
        ]
    [get_ports {data_in2 \         
    }]
}

set_output_delay -max 1.5 -clock [get_clocks clk] \     
    { \
    [get_ports {data_out1}] \
    [get_ports {data_out2}] \
    }

set_false_path -from [get_clocks {clk1}] \
    -to [get_clocks {clk2}]

set_input_delay -clock [get_clocks {clk}] \
    -max 3.0 \
    [get_ports { \
        data_in1 \
        data_in2 \
        data_in3 \
    }]

set_clock_groups -asynchronous -group {
    [get_clocks {clk1 clk2}]
} \
-group {
    [get_clocks {clk3 clk4}]
}
