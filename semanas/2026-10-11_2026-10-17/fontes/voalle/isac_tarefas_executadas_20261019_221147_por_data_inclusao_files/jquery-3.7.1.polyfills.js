/**
 * Polyfills para jQuery 3.7.1 - Compatibilidade Retroativa
 *
 * Fornece suporte temporário para métodos depreciados com avisos no console
 *
 * Polyfills incluídos:
 * 1. Detecção de navegador ($.browser)
 * 2. Manipuladores de eventos .live() e .die()
 * 3. Método $.curCSS()
 * 4. Método .andSelf()
 * 5. Tratamento de atributos booleanos com .attr()
 * 6. Adaptação para respostas AJAX vazias
 * 7. Polyfills para outerHeight() e outerWidth()
 *
 * AVISO: Estas são soluções temporárias e devem ser substituídas
 *        por alternativas modernas assim que possível
 *
 * Criado: 07/05/2025
 * Versão: 1.1
 */

(function($) {
    'use strict';

    // =============================================
    // SEÇÃO 1: POLYFILL DE DETECÇÃO DE NAVEGADOR
    // =============================================
    /**
     * Polyfill para $.browser (detecção de navegador depreciada)
     * Alternativa moderna: Utilizar feature detection
     *
     * Adiciona objeto $.browser com informações sobre:
     * - Tipo de navegador (mozilla, webkit, opera, msie, safari, chrome)
     * - Versão do navegador
     */
    if (!$.browser) {
        $.browser = {};
        var ua = navigator.userAgent.toLowerCase();

        // Detecção do tipo de navegador
        $.browser.mozilla = /mozilla/.test(ua) && !/webkit/.test(ua);
        $.browser.webkit = /webkit/.test(ua);
        $.browser.opera = /opera/.test(ua);
        $.browser.msie = /msie/.test(ua) || /trident/.test(ua);
        $.browser.safari = /safari/.test(ua) && !/chrome/.test(ua);
        $.browser.chrome = /chrome/.test(ua);

        // Detecção da versão
        $.browser.version = (function() {
            if ($.browser.msie && /trident/.test(ua)) {
                return ua.match(/rv:([\d.]+)/)[1];
            }
            var match = ua.match(/(webkit|opera|chrome|safari|firefox|msie)[\/\s]([\d.]+)/);
            return match ? match[2] : '0';
        })();

        // console.warn('[jQuery Polyfill] $.browser está depreciado. Use feature detection em vez disso.');
    }

    // =============================================
    // SEÇÃO 2: POLYFILLS PARA MANIPULADORES DE EVENTOS
    // =============================================
    /**
     * Polyfill para o método .live() (depreciado)
     * Alternativa moderna: $(document).on(evento, seletor, handler)
     *
     * @param {string} events - Eventos a serem tratados
     * @param {function} handler - Função de callback
     * @returns {jQuery} Objeto jQuery para encadeamento
     */
    if (!$.fn.live) {
        $.fn.live = function(events, handler) {
            // console.warn('[jQuery Polyfill] .live() está sendo executado - Método depreciado');

            // Trata múltiplos eventos
            if (typeof events === 'string' && events.indexOf(' ') > -1) {
                var eventList = events.split(' ');
                for (var i = 0; i < eventList.length; i++) {
                    if (this.selector) {
                        $(document).on(eventList[i], this.selector, handler);
                    } else {
                        // console.warn('[jQuery Polyfill] .live() sem seletor para múltiplos eventos', this, eventList[i], handler);
                    }
                }
                return this;
            }

            if (this.selector) {
                $(document).on(events, this.selector, handler);
            } else {
                // console.warn('[jQuery Polyfill] .live() sem seletor para envento', this, events, handler);
            }

            return this;
        };
    }

    /**
     * Polyfill para o método .die() (depreciado)
     * Alternativa moderna: $(document).off(evento, seletor)
     *
     * @param {string} events - Eventos a serem removidos
     * @param {function} handler - Função de callback específica
     * @returns {jQuery} Objeto jQuery para encadeamento
     */
    if (!$.fn.die) {
        $.fn.die = function(events, handler) {
            // console.warn('[jQuery Polyfill] .die() está sendo executado - Método depreciado', this.selector);

            // Trata múltiplos eventos
            if (typeof events === 'string' && events.indexOf(' ') > -1) {
                var eventList = events.split(' ');
                for (var i = 0; i < eventList.length; i++) {
                    if (this.selector) {
                        $(document).off(eventList[i], this.selector, handler);
                    } else {
                        // console.warn('[jQuery Polyfill] .die() sem seletor para múltiplos eventos', this, eventList[i], handler);
                    }
                }
                return this;
            }

            if (this.selector) {
                $(document).off(events, this.selector, handler);
            } else {
                // console.warn('[jQuery Polyfill] .die() sem seletor para envento', this, events, handler);
            }

            return this;
        };
    }

    // =============================================
    // SEÇÃO 3: POLYFILL PARA UTILITÁRIO CSS
    // =============================================
    /**
     * Polyfill para jQuery.curCSS() (depreciado)
     * Alternativa moderna: $(elemento).css(propriedade)
     *
     * @param {HTMLElement} element - Elemento alvo
     * @param {string} prop - Propriedade CSS
     * @param {string} val - Valor para setter (opcional)
     * @returns {string|jQuery} Valor da propriedade ou objeto jQuery
     */
    if (!jQuery.curCSS) {
        jQuery.curCSS = function(element, prop, val) {
            // console.warn('[jQuery Polyfill] $.curCSS() está sendo executado - Método depreciado');

            var $elem = jQuery(element);

            // Modo getter
            if (typeof val === "undefined" || val === "undefined") {
                // console.warn('[jQuery Polyfill] $.curCSS() está depreciado. Substitua por: $("' +
                //     (element.nodeName || 'elemento') + '").css("' + prop + '")');
                return $elem.css(prop);
            }

            // Modo setter
            // console.warn('[jQuery Polyfill] $.curCSS() está depreciado. Substitua por: $("' +
            //     (element.nodeName || 'elemento') + '").css("' + prop + '", "' + val + '")');

            return $elem.css(prop, val);
        };
    }

    // =============================================
    // SEÇÃO 4: POLYFILL PARA MÉTODOS DE TRAVERSIA
    // =============================================
    /**
     * Polyfill para .andSelf() (depreciado)
     * Alternativa moderna: .addBack()
     *
     * @returns {jQuery} Objeto jQuery para encadeamento
     */
    if (!$.fn.andSelf) {
        $.fn.andSelf = function() {
            // console.warn('[jQuery Polyfill] .andSelf() está sendo executado - Método depreciado');
            return this.addBack();
        };
    }

    // =============================================
    // SEÇÃO 5: TRATAMENTO DE ATRIBUTOS BOOLEANOS
    // =============================================
    /**
     * Polyfill para tratamento correto de atributos booleanos com .attr()
     * Alternativa moderna: Use .prop() para atributos booleanos
     */
    // Guarda referências originais
    var originalAttr = $.fn.attr;
    var originalRemoveAttr = $.fn.removeAttr;
    var originalVal = $.fn.val;

    // Lista de propriedades booleanas com tratamento especial
    var booleanProperties = {
        checked: true,
        selected: true,
        disabled: true,
        readonly: true,
        multiple: true,
        ismap: true
    };

    // Sobrescreve o método attr()
    $.fn.attr = function(name, value) {
        // Caso 1: É uma propriedade booleana
        if (booleanProperties[name]) {
            // console.warn('[jQuery Polyfill] .attr() para propriedade booleana "'+name+'" - Considere usar .prop()');

            if (typeof $.fn.prop === 'function') {
                if (arguments.length >= 2) {
                    return this.prop(name, value);
                }
                return this.prop(name);
            }
            return originalAttr.apply(this, arguments);
        }

        // Caso 2: É o atributo 'value'
        if (name === 'value') {
            // console.warn('[jQuery Polyfill] .attr("value") - Comportamento especial para inputs');

            // Modo getter (obter valor)
            if (arguments.length === 1) {
                // Para elementos de formulário, retorna o valor atual
                if (this.is('input, textarea, select')) {
                    return this.prop('value');
                }
                // Para outros elementos, comportamento padrão
                return originalAttr.call(this, name);
            }
            // Modo setter (definir valor)
            else if (arguments.length >= 2) {
                // Atualiza tanto a propriedade quanto o atributo
                this.prop('value', value);
                return originalAttr.call(this, name, value);
            }
        }

        // Caso 3: Comportamento padrão para outros atributos
        return originalAttr.apply(this, arguments);
    };

    /**
     * Polyfill para .removeProp()
     * Corrige comportamento para propriedades booleanas usando .prop() internamente
     *
     * @param {string} name - Nome da propriedade a ser removida
     * @returns {jQuery} Objeto jQuery para encadeamento
     */
    var originalRemoveProp = $.fn.removeProp;
    $.fn.removeProp = function(name) {
        if (booleanProperties[name]) {
            // console.warn('[jQuery Polyfill] .removeProp("'+name+'") - Propriedade booleana tratada');
            return this.prop(name, false);
        }
        return originalRemoveProp.apply(this, arguments);
    };

    // =============================================
    // SEÇÃO 6: POLYFILL PARA RESPOSTAS AJAX VAZIAS
    // =============================================
    /**
     * Adaptação para respostas AJAX vazias
     * Trata erros de parsing JSON quando a resposta está vazia mas com status 200
     */
    var originalAjax = $.ajax;
    $.ajax = function(settings) {
        // console.warn('[jQuery Polyfill] Adaptação AJAX ativa - Monitorando respostas vazias');

        if (settings && typeof settings === 'object' && 'error' in settings) {
            var originalError = settings.error;

            settings.error = function(jqXHR, textStatus, errorThrown) {
                // Trata erro de parsing JSON com status 200 e resposta vazia
                if (textStatus === 'parsererror' && jqXHR.status === 200 && jqXHR.responseText.trim() === '') {
                    // console.warn('[jQuery Polyfill] Resposta AJAX vazia tratada como sucesso');

                    if (settings.success) {
                        settings.success(null, 'success', jqXHR);
                    }
                    return;
                }

                // Chama o handler de erro original se existir
                if (typeof originalError === 'function') {
                    originalError.apply(this, arguments);
                }
            };
        }

        return originalAjax.apply(this, arguments);
    };

    // =============================================
    // SEÇÃO 7: POLYFILLS PARA OUTERHEIGHT E OUTERWIDTH
    // =============================================
    /**
     * Polyfill para outerHeight() sem parâmetro
     * Padroniza comportamento quando chamado sem argumentos (considera includeMargin=true)
     */
    var originalOuterHeight = $.fn.outerHeight;
    $.fn.outerHeight = function(includeMargin) {
        if (arguments.length === 0 || includeMargin == null) {
            // console.warn('[jQuery Polyfill] .outerHeight() chamado sem parâmetros - Padrão: includeMargin=true');
            includeMargin = true;
        }
        return originalOuterHeight.call(this, includeMargin);
    };

    /**
     * Polyfill para outerWidth() sem parâmetro
     * Padroniza comportamento quando chamado sem argumentos (considera includeMargin=true)
     */
    var originalOuterWidth = $.fn.outerWidth;
    $.fn.outerWidth = function(includeMargin) {
        if (arguments.length === 0) {
            // console.warn('[jQuery Polyfill] .outerWidth() chamado sem parâmetros - Padrão: includeMargin=true');
            includeMargin = true;
        }
        return originalOuterWidth.call(this, includeMargin);
    };

    var originalVal = $.fn.val;

    /**
     * Polyfill para o método .val()
     * Adiciona suporte para tratamento de selects com múltiplas opções (select[multiple])
     *
     * - Getter: Retorna o valor do elemento. Para selects múltiplos, retorna um array de valores.
     * - Setter: Define o valor do elemento sem alterar o comportamento original.
     *
     * Avisos:
     * - Em selects múltiplos, se o array de valores for vazio, retorna `null`.
     *
     * @param {string|Array} [value] - Valor a ser definido (opcional)
     * @returns {string|Array|null|jQuery} Valor do elemento ou objeto jQuery para encadeamento
     */
    $.fn.val = function(value) {
    // Caso SETTER
    if (arguments.length > 0) {
        return this.each(function() {
            var $el = $(this);

            if ($el.is('select') && !$el.is('select[multiple]') &&!Array.isArray(value)) {
                // Verifica se o valor existe entre as opções
                var hasOption = $el.find('option').filter(function() {
                    return $(this).val() == value;
                }).length > 0;

                if (!hasOption) {
                    // console.warn('[jQuery Polyfill] Valor "' + value + '" não é uma opção válida em <select>. Setando primeira opção.');
                    var firstOption = $el.find('option').first().val();
                    originalVal.call($el, firstOption);
                    return;
                }
            }

            // Se for válido ou não for select, seta normalmente
            originalVal.call($el, value);
        });
    }

        // Getter:
        var result = originalVal.call(this);

        // console.warn('[jQuery Polyfill] .val() chamado - Verifique se o elemento é um select[multiple]');
        if (this.is('select[multiple]')) {
            if (Array.isArray(result) && result.length === 0) {
                // console.warn('[jQuery Polyfill] .val() chamado - Array vazio para select[multiple]');

                return "";
            }
        }

        return result;
    };

    var originalOn = $.fn.on;

    /**
     * Polyfill para o método .on()
     * Adiciona suporte para o evento 'hover', substituindo-o por 'mouseenter'
     *
     * - Substitui automaticamente 'hover' por 'mouseenter' para compatibilidade com versões modernas do jQuery.
     *
     * Avisos:
     * - O evento 'hover' foi descontinuado em versões mais recentes do jQuery.
     *
     * @param {string} types - Tipos de eventos (ex.: 'click', 'hover')
     * @param {string} [selector] - Seletor para delegação de eventos (opcional)
     * @param {Object} [data] - Dados a serem passados para o evento (opcional)
     * @param {function} handler - Função de callback para o evento
     * @param {boolean} [one] - Indica se o evento deve ser executado apenas uma vez (opcional)
     * @returns {jQuery} Objeto jQuery para encadeamento
     */
    $.fn.on = function(types, selector, data, handler, /* internal */ one) {
        // Caso 'hover' seja o tipo de evento
        if (typeof types === 'string' && types.indexOf('hover') > -1) {
            // console.warn('[jQuery Polyfill] .on("hover") interceptado - substituindo por "mouseenter"');
            // Substitui 'hover' por 'mouseenter'
            types = types.replace(/\bhover\b/g, 'mouseenter');
        }
        return originalOn.call(this, types, selector, data, handler, one);
    };


    // Guarda referência original do método
    var originalHtml = $.fn.html;

    /**
     * Polyfill para o método .html()
     * Ajusta o comportamento do método .html() para garantir compatibilidade.
     *
     * - Setter: Mantém o comportamento padrão do método.
     * - Getter: Ajusta o retorno de `undefined` para `null` para maior consistência.
     *
     * Avisos:
     * - Este polyfill é temporário e deve ser substituído por alternativas modernas, se necessário.
     *
     * @param {string} [value] - Valor a ser definido no elemento (opcional).
     * @returns {string|null|jQuery} Conteúdo HTML do elemento ou objeto jQuery para encadeamento.
     */
    $.fn.html = function(value) {
        // Setter: mantém comportamento padrão
        if (arguments.length > 0) {
            // console.warn('[jQuery Polyfill] .html() chamado no modo setter');
            return originalHtml.call(this, value);
        }

        // Getter: ajusta retorno undefined => null
        var result = originalHtml.call(this);
        if (typeof result === 'undefined') {
            // console.warn('[jQuery Polyfill] .html() retornou undefined - Ajustando para null');
            return null;
        }

        // console.warn('[jQuery Polyfill] .html() chamado no modo getter');
        return result;
    };

    // Salva referência original do .load
    var originalLoad = $.fn.load;

    $.fn.load = function(url, params, callback) {
        if (typeof url === 'function' && this[0] === window) {
            // console.warn('[jQuery Polyfill] $(window).load(handler) é depreciado, usando $(window).on("load", handler)');

            // Se o documento já está carregado, chama o handler imediatamente
            if (document.readyState === 'complete') {
                url.call(window);
            } else {
                this.on('load', url);
            }
            return this;
        }
        return originalLoad.apply(this, arguments);
    };

    var _serializeArray = $.fn.serializeArray;

    $.fn.serializeArray = function () {
        return _serializeArray.call(this).filter(function (field) {
            // ignora selects múltiplos vazios e arrays sem valor
            if (/\[\]$/.test(field.name) && (field.value === "" || field.value == null)) {
                return false;
            }
            return true;
        });
    };

    $.fn.serialize = function () {
        return $.param(this.serializeArray());
    };

    $.fn.size = function() {
        return this.length;
    };

    // console.warn('[jQuery Polyfill] Todos os polyfills foram carregados - Verifique avisos individuais para métodos específicos');
})(jQuery);