$fn = 32;

pcb_w = 75.5;
pcb_h = 19.35;
pcb_d = 1.2;

bezel_w = 60.5;
bezel_h = 19;
bezel_d = 1.6;
bezel_offset_x = (pcb_w - bezel_w) / 2;
bezel_offset_y = (pcb_h - bezel_h) / 2;
bezel_offset_z = pcb_d;

va_w = 53.18;
va_h = 14.78;
va_d = bezel_d;
va_offset_x = ((bezel_w - va_w) / 2) + bezel_offset_x;
va_offset_y = ((bezel_h - va_h) / 2) + bezel_offset_y;
va_offset_z = bezel_offset_z;

aa_w = 51.18;
aa_h = 12.78;
aa_d = va_d;
aa_offset_x = ((va_w - aa_w) / 2) + va_offset_x;
aa_offset_y = ((va_h - aa_h) / 2) + va_offset_y;
aa_offset_z = va_offset_z;

mount_hole_d = 2.5;
mount_hole_offset_x = 1.7;
mount_hole_offset_y = 1.75;

union() {
  difference() {
    translate([0,0,0])
      color("#143324")
        cube([pcb_w, pcb_h, pcb_d]);
   
    translate([mount_hole_offset_x, mount_hole_offset_y, 0])
      cylinder(pcb_d, d = mount_hole_d);
    
    translate([pcb_w - mount_hole_offset_x, mount_hole_offset_y, 0])
      cylinder(pcb_d, d = mount_hole_d);
    
    translate([mount_hole_offset_x, pcb_h - mount_hole_offset_y, 0])
      cylinder(pcb_d, d = mount_hole_d);
      
    translate([pcb_w - mount_hole_offset_x, pcb_h - mount_hole_offset_y, 0])
      cylinder(pcb_d, d = mount_hole_d);
  }
  
  difference() {
    translate([bezel_offset_x, bezel_offset_y, bezel_offset_z])
      color("#080808")
        cube([bezel_w, bezel_h, bezel_d]);
  
    translate([va_offset_x, va_offset_y, va_offset_z])
      cube([va_w, va_h, va_d]);
  }
  
  difference() {
    translate([va_offset_x, va_offset_y, va_offset_z])
      color("#B7B7B7")
        cube([va_w, va_h, va_d]);
  
    translate([aa_offset_x, aa_offset_y, aa_offset_z])
      cube([aa_w, aa_h, aa_d]);
  }
  
  color("#C0C0C0")
    translate([aa_offset_x, aa_offset_y, aa_offset_z])
      cube([aa_w, aa_h, aa_d]);
}