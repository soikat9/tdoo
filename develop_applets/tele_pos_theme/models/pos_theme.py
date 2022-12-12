# -*- coding: utf-8 -*-

from attr import field
from tele import api, fields, models, tools

DEFAULT_PRIMARY = '#000000'
DEFAULT_SECONDARY = '#000000'

#SOLID theme variable
SOLID_COLOR_1 = '#0a7fe9'
SOLID_COLOR_2 = '#0a7fe9'
SOLID_COLOR_3 = '#f6f7fb'
SOLID_BUTTON_COLOR_1 = '#0a7fe9'
SOLID_BUTTON_COLOR_2 = '#0a7fe9'
SOLID_BUTTON_COLOR_3 = '#f6f7fb'

#GRADIENT theme variable
GRADIENT_COLOR_1 = '#1D7DD6'
GRADIENT_COLOR_2 = '#6CA5DB'
GRADIENT_COLOR_3 = '#ffffff'
GRADIENT_BUTTON_COLOR_1 = '#1D7DD6'
GRADIENT_BUTTON_COLOR_2 = '#6CA5DB'
GRADIENT_BUTTON_COLOR_3 = '#ffffff'

#Dark theme variable
DARK_COLOR_1 = '#949393'
DARK_COLOR_2 = '#585858'
DARK_COLOR_3 = '#3E3E3E'
DARK_BUTTON_COLOR_1 = '#1A83E4'
DARK_BUTTON_COLOR_2 = '#2A7CC8'
DARK_BUTTON_COLOR_3 = '#283142'





import base64
URL = '/tele_pos_theme/static/src/scss/pos_theme_variables.scss'
class RtPosThemeSettings(models.Model):
    """
    
    Customise the pos backend theme
    
    """

    _name = 'tele.pos.theme.settings'
    _description = 'POS Theme Settings'


    name = fields.Char(string="Name", required = True)
    
    theme_color_type = fields.Selection([ 
        ("solid",'Solid'),
        ("gradient",'Gradient'),
        ("dark",'Dark Mode'),       
        ],string="Theme Color Type", default="solid")  

    theme_primary_1_color = fields.Char(string="Theme Primary 1 Color")
    theme_primary_2_color = fields.Char(string="Theme Primary 2 Color")
    theme_secondary_color = fields.Char(string="Theme Secondary Color")
  
    
    theme_background_type = fields.Selection([
        ("none",'None'),
        # ("color",'Color'),
        ("image",'Image'),        
        ],string="Background Type", default="none")
    theme_background_color = fields.Char(string="Theme Background Color")
    theme_background_image = fields.Image(string="Theme Background Image")
    
    button_type = fields.Selection([
        ("style_1",'Style 1'),
        ("style_2",'Style 2'),
        ("style_3",'Style 3'),        
        ],string="Button Type", default="style_1")  
    
    button_color_type = fields.Selection([
        ("solid",'Solid'),
        ("gradient",'Gradient'),        
        ],string="Button Color Type", default="solid")  

    button_primary_1_color = fields.Char(string="Button Primary 1 Color")
    button_primary_2_color = fields.Char(string="Button Primary 2 Color")
    button_secondary_color = fields.Char(string="Secondary Button Color")
  
  
    is_use_google_font = fields.Boolean(string="Use Google Font?")
    google_font_family = fields.Char(string="Google font-family")
    
    theme_gradient_preview = fields.Html(compute='_theme_gradient_preview',
                          sanitize=False,
                          sanitize_tags=False,
                          sanitize_attributes=False,
                          sanitize_style=False,
                          sanitize_form=False,
                          strip_style=False,
                          strip_classes=False)  
  
  
    button_gradient_preview = fields.Html(compute='_button_gradient_preview',
                          sanitize=False,
                          sanitize_tags=False,
                          sanitize_attributes=False,
                          sanitize_style=False,
                          sanitize_form=False,
                          strip_style=False,
                          strip_classes=False)  
  
  
     
    @api.onchange('theme_color_type')
    def get_selection(self):
        if self.theme_color_type == "solid" :
            self.theme_primary_1_color = SOLID_COLOR_1
            self.theme_primary_2_color = SOLID_COLOR_2
            self.theme_secondary_color = SOLID_COLOR_3
            self.button_type = 'style_1'
            self.button_color_type = 'solid'
            self.button_primary_1_color = SOLID_BUTTON_COLOR_1
            self.button_primary_2_color = SOLID_BUTTON_COLOR_2
            self.button_secondary_color = SOLID_BUTTON_COLOR_3
        if self.theme_color_type == "gradient" :
            self.theme_primary_1_color = GRADIENT_COLOR_1
            self.theme_primary_2_color = GRADIENT_COLOR_2
            self.theme_secondary_color = GRADIENT_COLOR_3
            self.button_type = 'style_2'
            self.button_color_type = 'gradient'
            self.button_primary_1_color = GRADIENT_BUTTON_COLOR_1
            self.button_primary_2_color = GRADIENT_BUTTON_COLOR_2
            self.button_secondary_color = GRADIENT_BUTTON_COLOR_3    
        if self.theme_color_type == "dark" :
            self.theme_primary_1_color = DARK_COLOR_1
            self.theme_primary_2_color = DARK_COLOR_2
            self.theme_secondary_color = DARK_COLOR_3
            self.button_type = 'style_3'
            self.button_color_type = 'solid'
            self.button_primary_1_color = DARK_BUTTON_COLOR_1
            self.button_primary_2_color = DARK_BUTTON_COLOR_2
            self.button_secondary_color = DARK_BUTTON_COLOR_3
            

    @api.depends('theme_primary_1_color', 'theme_primary_2_color')
    def _theme_gradient_preview(self):
        for wizard in self:
            wizard.theme_gradient_preview = '''
            <div style="background-image: linear-gradient(to right, %s, %s);height:10px;"/>
            ''' % (self.theme_primary_1_color, self.theme_primary_2_color)
            
            
    @api.depends('button_primary_1_color', 'button_primary_2_color')
    def _button_gradient_preview(self):
        for wizard in self:
            wizard.button_gradient_preview = '''
            <div style="background-image: linear-gradient(to right, %s, %s);height:10px;"/>
            ''' % (self.button_primary_1_color, self.button_primary_2_color)
                             
  
    def action_apply_theme_settings(self):
        self.ensure_one()
        if self:
            content = """
            $tele_pos_theme_color_type:%(tele_pos_theme_color_type)s;
            $tele_pos_theme_primary_1_color:%(tele_pos_theme_primary_1_color)s;
            $tele_pos_theme_primary_2_color:%(tele_pos_theme_primary_2_color)s; 
            $tele_pos_theme_secondary_color:%(tele_pos_theme_secondary_color)s;                                  
            $tele_pos_theme_background_type:%(tele_pos_theme_background_type)s; 
            $tele_pos_theme_background_color:%(tele_pos_theme_background_color)s;              
            $tele_pos_button_type:%(tele_pos_button_type)s; 
            $tele_pos_button_color_type:%(tele_pos_button_color_type)s; 
            $tele_pos_button_primary_1_color:%(tele_pos_button_primary_1_color)s; 
            $tele_pos_button_primary_2_color:%(tele_pos_button_primary_2_color)s; 
            $tele_pos_button_secondary_color:%(tele_pos_button_secondary_color)s;                                     
            $tele_pos_is_use_google_font:%(tele_pos_is_use_google_font)s; 
            $tele_pos_google_font_family:%(tele_pos_google_font_family)s;
            """ % {
            'tele_pos_theme_color_type':self.theme_color_type,
            'tele_pos_theme_primary_1_color':self.theme_primary_1_color,  
            'tele_pos_theme_primary_2_color':self.theme_primary_2_color,
            'tele_pos_theme_secondary_color':self.theme_secondary_color,                                              
            'tele_pos_theme_background_type':self.theme_background_type, 
            'tele_pos_theme_background_color':self.theme_background_color, 
            'tele_pos_button_type':self.button_type, 
            'tele_pos_button_color_type':self.button_color_type, 
            'tele_pos_button_primary_1_color':self.button_primary_1_color, 
            'tele_pos_button_primary_2_color':self.button_primary_2_color, 
            'tele_pos_button_secondary_color':self.button_secondary_color,                                     
            'tele_pos_is_use_google_font':self.is_use_google_font, 
            'tele_pos_google_font_family':self.google_font_family,
            }


            
            datas = base64.b64encode((content or "\n").encode("utf-8"))

            # Check if the file to save had already been modified
            custom_attachment = self.env["ir.attachment"].sudo().search([
            ('url','=',URL),
            ])
            if custom_attachment.sudo():
                # attachment already exist then write values.
                custom_attachment.sudo().write({"datas": datas})
            else:
                # If not, create a new attachment for theme variables scss file
                new_attach = {
                    'name': 'pos_theme_variables.scss',
                    'type': "binary",
                    'mimetype': 'text/scss',
                    'datas': datas,
                    'url': URL,
                }
                self.env["ir.attachment"].sudo().create(new_attach)                
                      
#         return {
#             'type': 'ir.actions.act_url',
#             'target': 'self',
#             'url': '/',
#         }            
      
        
