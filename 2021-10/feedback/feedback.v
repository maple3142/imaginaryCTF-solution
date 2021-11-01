module feedback(win, init, clk, reset);
    output reg win;
    input [255:0] init;
    input clk, reset;

    reg [255:0] state;
    reg new;
    integer i;

    always @(posedge clk, posedge reset) begin
        if (reset) state <= init;
        else begin
            new <= 0;
            for (i = 0; i < 250; i += 1) begin
                if (i&1) begin
                    new ^= ^{2{state[i]}};
                end else begin
                    new ^= ^{7{state[i]}};
                end  
            end
            state <= {new, state[255:1]};
        end
        win <= (state == 256'h98cb7f18bb2e8f0fdc857d6bac4878f4be43b6c4ac87ad212e3e1566929736c0);
    end
endmodule

module main;
    integer i;
    wire win;
    reg clk, reset;
    reg [255:0] flag = 256'h696374667b00000000000000000000000000000000000000000000000000007d;
    // note that there are many inputs that will output "correct"
    // only the one in flag format is the valid
    feedback flagchecker(win, flag, clk, reset);

    initial begin
        $display("Checking the flag entered in the flag register.");
        $display("This may take a little bit of time...");
        clk <= 0;
        reset <= 0;
        #10;
        reset <= 1;
        #10;
        reset <= 0;
        for (i = 0; i < 500*256; i+=1) begin
        #20;
            if (win) begin
                $display("Correct!");
                $finish;
            end
            if (i%(256*50)==0) $display("%d%% done", i/(256*5));
        end
        $display("Doesn't look right to me...");
        $finish;
    end

    always
        #10 clk = ~clk;
endmodule