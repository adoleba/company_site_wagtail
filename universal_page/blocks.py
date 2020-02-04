from wagtail.core import blocks


class WhiteHeaderWithButton(blocks.StreamBlock):
    header_text = blocks.CharBlock(classname="header text")
    button_text = blocks.CharBlock(classname="header text")
    button_url = blocks.PageChooserBlock(classname="internal url")

    class Meta:
        template = 'universal_page/blocks/white_header_with_button.html'


class ThreeColumnsWithHeaders(blocks.StreamBlock):
    column_no_1_header = blocks.CharBlock(classname="header text column no 1")
    column_no_1_text = blocks.RichTextBlock(classname="text column no 1")
    column_no_2_header = blocks.CharBlock(classname="header text column no 2")
    column_no_2_text = blocks.RichTextBlock(classname="text column no 2")
    column_no_3_header = blocks.CharBlock(classname="header text column no 3")
    column_no_3_text = blocks.RichTextBlock(classname="text column no 3")

    class Meta:
        template = 'universal_page/blocks/three_columns_with_headers.html'


class Faq(blocks.StreamBlock):
    question = blocks.CharBlock(classname="question")
    answer = blocks.RichTextBlock(classname="answer")

    class Meta:
        template = 'universal_page/blocks/faq.html'


class ParagraphWithHeader(blocks.StreamBlock):
    header_text = blocks.RichTextBlock(classname="header text")
    paragraph_text = blocks.RichTextBlock(classname="paragraph text")

    class Meta:
        template = 'universal_page/blocks/paragraph_with_header.html'
